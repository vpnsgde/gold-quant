#!/usr/bin/env python3
"""
scripts/model_lstm_gru.py

LSTM+GRU pipeline for XAUUSD 5m forecasting.
- Uses last 100k records from dataset/xauusd_5m.csv
- Forecasts next 50 steps with Monte Carlo Dropout to estimate confidence interval
- Plots last 200 bars + forecast mean and CI
- Logs to logs/model_lstm_gru.txt
"""

import os
import logging
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# === Configurations ===
DATA_PATH = "dataset/xauusd_5m.csv"
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "model_lstm_gru.txt")

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)

SUBSAMPLE_SIZE = 100_000
FORECAST_STEPS = 50
LOOKBACK = 50
N_MC = 100  # Monte Carlo simulations for CI
CONF_LEVEL = 0.9  # 90% CI
HISTORY_WINDOW = 200  # number of past bars to plot

# === Logging ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [INFO] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w")
    ]
)

# === Utilities ===
def load_data(csv_file, n_records=SUBSAMPLE_SIZE):
    logging.info("Loading CSV from %s", csv_file)
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    df = pd.read_csv(csv_file)
    if "Close" not in df.columns:
        raise ValueError("CSV must contain 'Close' column")
    logging.info("CSV loaded with %d rows", len(df))
    series = df["Close"].values[-n_records:].reshape(-1,1)
    logging.info("Using last %d records for modeling", len(series))
    df_used = df.tail(n_records).copy()
    df_used["datetime"] = pd.to_datetime(df_used["Date"] + " " + df_used["Time"], format="%Y.%m.%d %H:%M")
    df_used.set_index("datetime", inplace=True)
    return series, df_used

def create_dataset(series, lookback=LOOKBACK):
    X, y = [], []
    for i in range(len(series) - lookback):
        X.append(series[i:i+lookback, 0])
        y.append(series[i+lookback, 0])
    X = np.array(X)
    y = np.array(y)
    return X.reshape((X.shape[0], X.shape[1], 1)), y

def build_model(lookback):
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=(lookback,1)))
    model.add(Dropout(0.2))
    model.add(GRU(64))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")
    return model

def forecast_with_uncertainty(model, last_window, n_steps, scaler, n_sim=N_MC):
    forecasts = []
    for sim in range(n_sim):
        preds = []
        window = last_window.copy()
        for _ in range(n_steps):
            pred = model(window, training=True).numpy()[0,0]  # MC Dropout
            preds.append(pred)
            window = np.roll(window, -1, axis=1)
            window[0,-1,0] = pred
        forecasts.append(preds)
    forecasts = np.array(forecasts)
    mean_forecast = forecasts.mean(axis=0)
    lower = np.percentile(forecasts, (1-CONF_LEVEL)/2*100, axis=0)
    upper = np.percentile(forecasts, (1+CONF_LEVEL)/2*100, axis=0)
    # inverse transform
    mean_forecast = scaler.inverse_transform(mean_forecast.reshape(-1,1)).flatten()
    lower = scaler.inverse_transform(lower.reshape(-1,1)).flatten()
    upper = scaler.inverse_transform(upper.reshape(-1,1)).flatten()
    return mean_forecast, lower, upper

# === Main ===
if __name__ == "__main__":
    try:
        series, df_used = load_data(DATA_PATH)
    except Exception as e:
        logging.error("Error loading data: %s", e)
        exit(1)

    # Normalize
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled = scaler.fit_transform(series)

    # Create sequences
    X, y = create_dataset(scaled)
    split = int(len(X)*0.8)
    X_train, y_train = X[:split], y[:split]
    X_val, y_val = X[split:], y[split:]

    logging.info("Building LSTM+GRU model...")
    model = build_model(LOOKBACK)

    logging.info("Training model...")
    model.fit(X_train, y_train, validation_data=(X_val, y_val),
              epochs=10, batch_size=64, verbose=1)

    last_window = X[-1:].copy()
    logging.info("Forecasting next %d steps with Monte Carlo Dropout...", FORECAST_STEPS)
    mean_forecast, lower, upper = forecast_with_uncertainty(model, last_window, FORECAST_STEPS, scaler)

    # Build forecast datetime index (5-minute interval)
    forecast_index = pd.date_range(df_used.index[-1], periods=FORECAST_STEPS+1, freq="5T")[1:]

    # Plot last HISTORY_WINDOW bars + forecast
    plot_tail = df_used["Close"].tail(HISTORY_WINDOW)
    plt.figure(figsize=(12,6))
    plt.plot(plot_tail.index, plot_tail.values, label=f"Historical (last {HISTORY_WINDOW})")
    plt.plot(forecast_index, mean_forecast, label="Forecast mean")
    plt.fill_between(forecast_index, lower, upper, color="gray", alpha=0.3, label=f"{int(CONF_LEVEL*100)}% CI")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("XAUUSD 5m LSTM+GRU Forecast (mean + CI)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    logging.info("Forecasted prices (mean and 90%% CI):")
    for i in range(FORECAST_STEPS):
        logging.info("Step %d: %.4f [%.4f, %.4f]", i+1, mean_forecast[i], lower[i], upper[i])
