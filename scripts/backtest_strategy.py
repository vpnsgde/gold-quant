#!/usr/bin/env python3
"""
scripts/backtest_strategy.py

Backtrader script for EMA/RSI/MACD strategy on XAUUSD 5m data.
- EMA 8/13 crossover
- RSI filter
- MACD confirmation
- Handles ZeroDivisionError for indicators
- Logs to /backtest/backtest_strategy.txt
- Saves plot to /backtest/strategy_plot.png
"""

import os
import logging
import pandas as pd
import backtrader as bt
import matplotlib.pyplot as plt

# === Configurations ===
DATA_PATH = "dataset/xauusd_5m.csv"
BACKTEST_DIR = "backtest"
os.makedirs(BACKTEST_DIR, exist_ok=True)
LOG_FILE = os.path.join(BACKTEST_DIR, "backtest_strategy.txt")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [INFO] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode="w")
    ]
)

# === Strategy ===
class EMA_RSI_MACD(bt.Strategy):
    params = dict(
        ema_fast=8,
        ema_slow=13,
        rsi_period=14,
        rsi_overbought=70,
        rsi_oversold=30,
        macd_fast=12,
        macd_slow=26,
        macd_signal=9
    )

    def __init__(self):
        self.ema_fast = bt.ind.EMA(self.data.close, period=self.p.ema_fast)
        self.ema_slow = bt.ind.EMA(self.data.close, period=self.p.ema_slow)
        self.rsi = bt.ind.RSI_SMA(self.data.close, period=self.p.rsi_period, safediv=True)
        self.macd = bt.ind.MACD(
            self.data.close,
            period_me1=self.p.macd_fast,
            period_me2=self.p.macd_slow,
            period_signal=self.p.macd_signal
        )
        self.cross = bt.ind.CrossOver(self.ema_fast, self.ema_slow)

    def next(self):
        # skip until indicators are ready
        if len(self.data) < max(self.p.ema_slow, self.p.rsi_period, self.p.macd_slow):
            return

        if not self.position:
            if self.cross > 0 and self.rsi < self.p.rsi_overbought and self.macd.macd > self.macd.signal:
                self.buy()
                logging.info(f"BUY at {self.data.datetime.datetime(0)} price {self.data.close[0]:.2f}")
            elif self.cross < 0 and self.rsi > self.p.rsi_oversold and self.macd.macd < self.macd.signal:
                self.sell()
                logging.info(f"SELL at {self.data.datetime.datetime(0)} price {self.data.close[0]:.2f}")
        else:
            if self.position.size > 0 and self.cross < 0:
                self.close()
            elif self.position.size < 0 and self.cross > 0:
                self.close()

# === Main ===
if __name__ == "__main__":
    logging.info("Loading CSV data from %s", DATA_PATH)
    if not os.path.exists(DATA_PATH):
        logging.error("CSV file not found: %s", DATA_PATH)
        exit(1)

    df = pd.read_csv(DATA_PATH)
    if len(df) < 26:
        logging.error("Not enough data for EMA/MACD/RSI calculation")
        exit(1)

    # Prepare Backtrader feed
    df_bt = df.copy()
    df_bt["datetime"] = pd.to_datetime(df_bt["Date"] + " " + df_bt["Time"], format="%Y.%m.%d %H:%M")
    df_bt.set_index("datetime", inplace=True)
    df_bt = df_bt[["Open","High","Low","Close","Volume"]]

    data = bt.feeds.PandasData(dataname=df_bt, timeframe=bt.TimeFrame.Minutes, compression=5)

    # Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.addstrategy(EMA_RSI_MACD)
    cerebro.adddata(data)
    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.0005)  # 0.05%

    logging.info("Starting backtest...")
    cerebro.run()
    logging.info("Backtest completed. Final Portfolio Value: %.2f", cerebro.broker.getvalue())

    # Plot and save figure
    logging.info("Saving plot to backtest folder")
    plt_path = os.path.join(BACKTEST_DIR, "strategy_plot.png")
    fig = cerebro.plot(style='candle')[0][0]
    fig.savefig(plt_path)
    logging.info("Plot saved at %s", plt_path)
