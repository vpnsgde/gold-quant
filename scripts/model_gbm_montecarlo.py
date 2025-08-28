#!/usr/bin/env python3
"""
scripts/model_gbm_mc.py

Monte Carlo simulation using Geometric Brownian Motion (GBM) for XAUUSD 5m.
- Use last 100k records for estimation.
- Simulate N_MC paths and compute mean and confidence intervals.
- Forecast next FORECAST_STEPS bars (default 50).
- Save forecast CSV to tmp/forecast_gbm_mc.csv and logs to logs/model_gbm_mc.txt.
"""

import os
import logging

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

# === Configurations ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "model_gbm_mc.txt")

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)
FORECAST_OUT_CSV = os.path.join(TMP_DIR, "forecast_gbm_mc.csv")

DATA_PATH = "dataset/xauusd_5m.csv"
SUBSAMPLE_SIZE = 100_000  # use last 100k rows for estimation
FORECAST_STEPS = 50
HISTORY_WINDOW = 200       # for plotting last bars
N_MC = 1000                # number of Monte Carlo paths
CONF_LEVEL = 0.95

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
    """Load CSV with columns: Date,Time,Open,High,Low,Close,Volume"""
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="%Y.%m.%d %H:%M")
    df = df.set_index("datetime")
    df["Close"] = df["Close"].astype(float)
    return df

def prepare_log_returns(price_series: pd.Series) -> pd.Series:
    """Compute log returns"""
    return np.log(price_series).diff().dropna()

def monte_carlo_gbm(last_price: float, mu: float, sigma: float, steps: int, n_paths: int):
    """
    Simulate GBM price paths
    """
    dt = 1  # assume 1 step = 5 min interval, units consistent with mu/sigma
    paths = np.zeros((steps, n_paths))
    paths[0, :] = last_price

    for t in range(1, steps):
        Z = np.random.standard_normal(n_paths)
        paths[t, :] = paths[t-1, :] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return paths

def compute_statistics(paths: np.ndarray, conf_level=0.95):
    """
    Compute mean, lower, upper percentiles across Monte Carlo paths
    """
    mean_path = np.mean(paths, axis=1)
    lower_path = np.percentile(paths, 50 - conf_level*50, axis=1)
    upper_path = np.percentile(paths, 50 + conf_level*50, axis=1)
    return mean_path, lower_path, upper_path

# === Main flow ===
if __name__ == "__main__":
    logging.info("Loading data from %s", DATA_PATH)
    df = load_price_csv(DATA_PATH)
    logging.info("Loaded %d rows", len(df))

    # Subsample last N rows
    if SUBSAMPLE_SIZE is not None and len(df) > SUBSAMPLE_SIZE:
        df_used = df.tail(SUBSAMPLE_SIZE).copy()
        logging.info("Using last %d rows for estimation.", SUBSAMPLE_SIZE)
    else:
        df_used = df.copy()
        logging.info("Using full data (size %d) for estimation.", len(df_used))

    # Compute log returns
    log_ret = prepare_log_returns(df_used["Close"])
    mu = log_ret.mean()  # drift
    sigma = log_ret.std()  # volatility
    logging.info("Estimated drift (mu)=%.6f, volatility (sigma)=%.6f", mu, sigma)

    last_price = df_used["Close"].iloc[-1]

    # Run Monte Carlo simulation
    logging.info("Running Monte Carlo GBM with %d paths, %d steps.", N_MC, FORECAST_STEPS)
    paths = monte_carlo_gbm(last_price, mu, sigma, steps=FORECAST_STEPS, n_paths=N_MC)

    # Compute mean and confidence intervals
    mean_path, lower_path, upper_path = compute_statistics(paths, conf_level=CONF_LEVEL)

    # Build datetime index for forecast
    forecast_index = pd.date_range(df_used.index[-1], periods=FORECAST_STEPS + 1, freq="5T")[1:]

    # Prepare DataFrame
    forecast_df = pd.DataFrame({
        "price_mean": mean_path,
        "price_lower": lower_path,
        "price_upper": upper_path
    }, index=forecast_index)

    # Save to CSV
    forecast_df.to_csv(FORECAST_OUT_CSV, index=True)
    logging.info("Forecast saved to %s", FORECAST_OUT_CSV)

    # Plot last HISTORY_WINDOW + forecast mean + CI
    try:
        plot_tail = df_used["Close"].tail(HISTORY_WINDOW)
        plt.figure(figsize=(12,6))
        plt.plot(plot_tail.index, plot_tail.values, label=f"Historical (last {HISTORY_WINDOW})")
        plt.plot(forecast_df.index, forecast_df["price_mean"].values, label="Forecast mean")
        plt.fill_between(forecast_df.index,
                         forecast_df["price_lower"].values,
                         forecast_df["price_upper"].values,
                         color="gray", alpha=0.3, label=f"{int(CONF_LEVEL*100)}% CI")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("XAUUSD 5m GBM Monte Carlo Forecast (mean + CI)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.warning("Plotting failed: %s", e)

    logging.info("Script finished.")
