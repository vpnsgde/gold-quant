# Gold Quant Project

## Overview

This project is a comprehensive quantitative trading framework for **XAUUSD (Gold) data**. It integrates multiple forecasting and backtesting strategies using historical gold price data at various timeframes (1m, 5m, 15m, 30m, 1h, daily). The project includes classic time-series models, machine learning approaches, Monte Carlo simulations, and strategy backtesting using Backtrader.

## Project Structure

```
├── backtest                # Backtesting results and logs
├── database                # (Optional) local database storage
├── dataset                 # Historical XAUUSD data CSV files
├── docs                    # Documentation
├── logs                    # Log files for modeling and backtesting
├── notebooks               # Jupyter notebooks (analysis, experiments)
├── scripts                 # Python scripts for modeling and backtesting
├── tmp                     # Temporary files (forecast results, images)
├── README.md               # Project overview (this file)
└── requirements.txt        # Python dependencies
```

### Dataset

* `dataset/xauusd_5m.csv`: primary dataset used for backtesting and modeling.
* Other CSVs contain historical gold prices for 1m, 15m, 30m, 1h, daily.
* 1m data split by year/month for easier management.

### Logs

* `logs/model_arima_garch.txt`: logs for ARIMA+GARCH forecasting.
* `logs/model_gbm_mc.txt`: logs for Monte Carlo GBM simulations.
* `logs/model_lstm_gru.txt`: logs for LSTM/GRU deep learning models.
* `logs/model_transformer.txt`: logs for Transformer-based forecasting.
* `logs/backtest_strategy.txt`: logs for EMA/RSI/MACD strategy backtesting.

### Temporary Outputs

* Forecast CSVs and plot images stored in `tmp/`, including:

  * `forecast_arima_garch.csv`
  * `forecast_gbm_mc.csv`
  * `img_model_arima_garch.png`
  * `img_model_gbm_montecarlo.png`
  * `img_run.png`

## Scripts

All scripts are located in the `scripts/` folder:

| Script                    | Description                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| `model_arima_garch.py`    | Forecast XAUUSD prices using ARIMA + GARCH with 50-step ahead forecast and confidence interval.          |
| `model_gbm_montecarlo.py` | Monte Carlo simulation using Geometric Brownian Motion to generate multiple possible future price paths. |
| `model_lstm_gru.py`       | Deep learning model using LSTM/GRU to predict future XAUUSD prices.                                      |
| `model_transformer.py`    | Transformer-based model capturing complex sequential patterns for price forecasting.                     |
| `backtest_strategy.py`    | Backtesting EMA/RSI/MACD strategy using Backtrader, logging trades, and saving plots.                    |

## Features

1. **Multi-timeframe historical data**: 1m, 5m, 15m, 30m, 1h, daily.
2. **Forecasting techniques**:

   * ARIMA + GARCH for volatility-aware predictions.
   * Monte Carlo GBM for multiple scenario forecasting.
   * LSTM/GRU neural networks.
   * Transformer-based sequence modeling.
3. **Backtesting**:

   * EMA crossover (8/13) strategy with RSI and MACD filters.
   * Logging trades and portfolio value.
   * Saving candle plots with trades.
4. **Logging & reproducibility**:

   * Every model and backtest logs detailed progress and results.
   * Temporary CSV outputs for further analysis.

## Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Forecasting with ARIMA+GARCH:

```bash
python scripts/model_arima_garch.py
```

3. Monte Carlo GBM simulation:

```bash
python scripts/model_gbm_montecarlo.py
```

4. LSTM/GRU forecasting:

```bash
python scripts/model_lstm_gru.py
```

5. Transformer forecasting:

```bash
python scripts/model_transformer.py
```

6. Backtest EMA/RSI/MACD strategy:

```bash
python scripts/backtest_strategy.py
```

All logs will appear in the `logs/` folder, and plots or CSV outputs will be saved in `tmp/` or `backtest/`.

## Notes

* Use subsampling or batching for large datasets to avoid memory issues.
* Models are configurable in their respective scripts (lookback periods, forecast horizon, neural network layers, dropout rates, etc.).
* Confidence intervals in forecasts are computed using Monte Carlo simulations or ARIMA+GARCH error variance.

## Future Enhancements

* Parameter optimization for strategies using grid search.
* Automated reporting of performance metrics (Sharpe ratio, max drawdown).
* Integration with live trading APIs for strategy deployment.
* Additional feature engineering for deep learning models (volume, volatility, technical indicators).
