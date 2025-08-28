#!/usr/bin/env python3
"""
scripts/model_arima_garch.py

ARIMA + GARCH pipeline for short-term price forecasting (XAUUSD 5m).
- Use last 100k records for modeling by default.
- Grid search ARIMA (sequential, light) by AIC.
- Fit GARCH(1,1) on ARIMA residuals.
- Forecast next N steps (default 50) and compute 95% CI using GARCH variance forecasts.
- Save forecast CSV to tmp/forecast_arima_garch.csv and logs to logs/model_arima_garch.txt.
"""

import os
import logging
from itertools import product

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

warnings.filterwarnings("ignore")

# === Configurations ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "model_arima_garch.txt")

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)
FORECAST_OUT_CSV = os.path.join(TMP_DIR, "forecast_arima_garch.csv")

DATA_PATH = "dataset/xauusd_5m.csv"
SUBSAMPLE_SIZE = 100_000  # use last 100k rows for model selection/training
FORECAST_STEPS = 50       # predict next 50 bars
HISTORY_WINDOW = 200      # plot last 200 bars + forecast
ARIMA_P_RANGE = (0, 4)
ARIMA_D_RANGE = (0, 1)
ARIMA_Q_RANGE = (0, 4)
GARCH_P = 1
GARCH_Q = 1
CONF_LEVEL = 0.95        # confidence interval level
REFIT_ON_FULL = False    # if True, refit final models on full series (may be expensive)

# === Logging ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w")
    ]
)


# === Utilities ===
def load_price_csv(path: str) -> pd.DataFrame:
    """
    Load CSV with columns: Date,Time,Open,High,Low,Close,Volume
    Date format expected: YYYY.MM.DD
    Time format expected: HH:MM
    """
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="%Y.%m.%d %H:%M")
    df = df.set_index("datetime")
    df["Close"] = df["Close"].astype(float)
    return df


def prepare_log_returns(price_series: pd.Series) -> pd.Series:
    """Compute log returns and drop NaNs."""
    return np.log(price_series).diff().dropna()


def arima_grid_search(series: pd.Series, p_range, d_range, q_range):
    """
    Sequential grid search for ARIMA by AIC.
    Returns best_order and fitted ARIMA results object.
    """
    best_aic = np.inf
    best_order = None
    best_res = None

    orders = list(product(range(p_range[0], p_range[1] + 1),
                          range(d_range[0], d_range[1] + 1),
                          range(q_range[0], q_range[1] + 1)))

    logging.info("Starting sequential ARIMA grid search over %d orders.", len(orders))

    for order in orders:
        try:
            # Fit ARIMA on pandas Series
            model = ARIMA(series, order=order)
            res = model.fit(method_kwargs={"warn_convergence": False})
            aic = float(res.aic)
            logging.info("ARIMA%s fitted, AIC=%.4f", order, aic)
            if aic < best_aic:
                best_aic = aic
                best_order = order
                best_res = res
        except Exception as e:
            logging.debug("ARIMA%s failed: %s", order, e)
            continue

    if best_order is None:
        raise RuntimeError("ARIMA grid search failed for all orders.")

    logging.info("ARIMA grid search completed. Best order: %s, Best AIC: %.4f", best_order, best_aic)
    return best_order, best_res


def fit_garch_on_residuals(residuals: pd.Series, p=1, q=1):
    """
    Fit a GARCH(p,q) on residuals. Returns fitted arch model.
    If fit fails, raise exception for caller to handle.
    """
    try:
        am = arch_model(residuals * 1.0, vol="GARCH", p=p, q=q, dist="normal", mean="Zero")
        res = am.fit(disp="off", show_warning=False)
        logging.info("GARCH(%d,%d) fitted. AIC: %.4f", p, q, res.aic)
        return res
    except Exception as e:
        logging.warning("GARCH fit failed: %s", e)
        raise


def forecast_arima_garch(arima_res, garch_res, steps, last_price):
    """
    Produce ARIMA mean forecasts (returns) and GARCH variance forecasts, then reconstruct price forecast.
    Returns DataFrame with columns: step, mean_return, var, price_mean, price_lower, price_upper
    """
    # ARIMA mean forecast of returns
    mean_forecast = arima_res.get_forecast(steps=steps).predicted_mean
    # GARCH variance forecast (horizon steps)
    # arch's forecast object: .variance is a DataFrame with index of last in-sample and columns 1..horizon
    garch_fore = garch_res.forecast(horizon=steps, reindex=False)
    # extract variance forecasts as 1D array length steps
    try:
        var_fore = garch_fore.variance.values[-1]  # shape (horizon,)
    except Exception:
        # Fallback: use constant variance equal to residual variance
        var_fore = np.repeat(np.var(garch_res.std_resid), steps)
        logging.warning("Failed to extract GARCH variance forecast, using constant variance fallback.")

    # Prepare DataFrame for outputs
    z = abs(np.round(np.sqrt(2) * erfcinv(2 * (1 - CONF_LEVEL)), 6)) if False else None
    # Instead of erfcinv (not available), use standard normal quantile from scipy if available.
    try:
        from scipy.stats import norm
        z_value = norm.ppf(0.5 + CONF_LEVEL / 2.0)
    except Exception:
        # fallback to 1.96 for 95%
        z_value = 1.96

    # Reconstruct prices iteratively
    prices_mean = []
    prices_lower = []
    prices_upper = []
    current_price = float(last_price)

    for i in range(steps):
        mu = float(mean_forecast.iloc[i]) if hasattr(mean_forecast, "iloc") else float(mean_forecast[i])
        sigma2 = float(var_fore[i])
        sigma = np.sqrt(max(sigma2, 0.0))

        # predicted multiplicative factor for one-step: exp(mu)
        price_next_mean = current_price * np.exp(mu)
        # compute CI on return scale and then map to price
        upper_return = mu + z_value * sigma
        lower_return = mu - z_value * sigma
        price_next_upper = current_price * np.exp(upper_return)
        price_next_lower = current_price * np.exp(lower_return)

        prices_mean.append(price_next_mean)
        prices_upper.append(price_next_upper)
        prices_lower.append(price_next_lower)

        # advance current_price for next step using mean forecast (this produces a single path)
        current_price = price_next_mean

    df_out = pd.DataFrame({
        "step": np.arange(1, steps + 1),
        "mean_return": np.asarray(mean_forecast).astype(float),
        "var": np.asarray(var_fore).astype(float),
        "price_mean": np.asarray(prices_mean),
        "price_lower": np.asarray(prices_lower),
        "price_upper": np.asarray(prices_upper),
    })
    return df_out


# helper: if scipy not available, we used fallback z=1.96; otherwise use norm.ppf
try:
    from scipy.stats import norm
    DEFAULT_Z = norm.ppf(0.5 + CONF_LEVEL / 2.0)
except Exception:
    DEFAULT_Z = 1.96


# === Main flow ===
if __name__ == "__main__":
    logging.info("Loading data from %s", DATA_PATH)
    df = load_price_csv(DATA_PATH)
    logging.info("Loaded price series with %d rows", len(df))

    # Subsample last N rows for modeling
    if SUBSAMPLE_SIZE is not None and len(df) > SUBSAMPLE_SIZE:
        df_used = df.tail(SUBSAMPLE_SIZE).copy()
        logging.info("Using last %d rows for modeling.", SUBSAMPLE_SIZE)
    else:
        df_used = df.copy()
        logging.info("Using full data for modeling (size %d).", len(df_used))

    # Prepare log returns
    log_ret = prepare_log_returns(df_used["Close"])
    logging.info("Prepared log returns, length %d", len(log_ret))

    # Grid search ARIMA on log returns (sequential)
    best_order, best_arima_res = arima_grid_search(log_ret, ARIMA_P_RANGE, ARIMA_D_RANGE, ARIMA_Q_RANGE)

    # Optionally refit on full series if requested
    if REFIT_ON_FULL:
        logging.info("Refitting ARIMA%s on full log-return series.", best_order)
        full_log_ret = prepare_log_returns(df["Close"])
        best_arima_res = ARIMA(full_log_ret, order=best_order).fit(method_kwargs={"warn_convergence": False})
        model_series_for_garch = best_arima_res.resid
        last_close_price = df["Close"].iloc[-1]
    else:
        model_series_for_garch = best_arima_res.resid
        last_close_price = df_used["Close"].iloc[-1]

    # Fit GARCH(1,1) on ARIMA residuals
    try:
        garch_res = fit_garch_on_residuals(model_series_for_garch, p=GARCH_P, q=GARCH_Q)
    except Exception:
        # If GARCH fails, fall back to using residual variance (constant volatility)
        logging.warning("GARCH fit failed, using constant variance fallback.")
        class DummyGarch:
            def __init__(self, resid):
                self.std_resid = resid / np.std(resid)
            def forecast(self, horizon, reindex=False):
                class VF:
                    def __init__(self, var):
                        self.variance = pd.DataFrame([var])
                var = np.var(model_series_for_garch)
                return VF(np.repeat(var, horizon))
        garch_res = DummyGarch(model_series_for_garch)

    # Forecast next steps and reconstruct price path with CI
    logging.info("Forecasting next %d steps.", FORECAST_STEPS)
    forecast_df = forecast_arima_garch(best_arima_res, garch_res, steps=FORECAST_STEPS, last_price=last_close_price)

    # Build timestamp index for forecast points (5-minute frequency)
    forecast_index = pd.date_range(df_used.index[-1], periods=FORECAST_STEPS + 1, freq="5T")[1:]
    forecast_df["datetime"] = forecast_index
    forecast_df = forecast_df.set_index("datetime")

    # Save forecast to CSV
    forecast_df_out = forecast_df[["price_mean", "price_lower", "price_upper", "mean_return", "var"]].copy()
    forecast_df_out.to_csv(FORECAST_OUT_CSV, index=True)
    logging.info("Forecast saved to %s", FORECAST_OUT_CSV)

    # Plot last HISTORY_WINDOW bars plus forecast mean and CI
    try:
        plot_tail = df_used["Close"].tail(HISTORY_WINDOW)
        plt.figure(figsize=(12, 6))
        plt.plot(plot_tail.index, plot_tail.values, label=f"Historical (last {HISTORY_WINDOW})")
        plt.plot(forecast_df_out.index, forecast_df_out["price_mean"].values, label="Forecast mean")
        plt.fill_between(forecast_df_out.index,
                         forecast_df_out["price_lower"].values,
                         forecast_df_out["price_upper"].values,
                         color="gray", alpha=0.3, label=f"{int(CONF_LEVEL*100)}% CI")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("XAUUSD 5m ARIMA+GARCH Forecast (mean and CI)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.warning("Plotting failed: %s", e)

    logging.info("Script finished. Best ARIMA order: %s", best_order)
    logging.info("First forecasted mean prices:\n%s", forecast_df_out["price_mean"].head(10).to_string(index=True))
