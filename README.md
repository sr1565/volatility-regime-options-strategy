# volatility-regime-options-strategy
Research-driven backtest of a volatility regime–filtered options strategy using realized volatility, Black–Scholes pricing, and Monte Carlo risk analysis.
# Volatility Regime–Based Options Strategy

## Overview
This repository contains a quantitative research project that investigates whether volatility regime detection can improve the risk-adjusted performance of a systematic short-volatility options strategy.

The project implements a reproducible Python framework to detect market volatility regimes, price European options using the Black–Scholes model, backtest a regime-filtered short-strangle strategy, and evaluate performance using statistical and Monte Carlo–based risk analysis. The focus of this work is methodological research rather than live trading or performance claims.

## Research Question
Can filtering options trades based on volatility regimes reduce drawdowns and improve risk-adjusted returns compared to an unfiltered short-volatility strategy?

## Data
- Daily adjusted close prices for SPY (S&P 500 ETF)
- Risk-free rate proxy (constant or historical, configurable)
- Optional comparison using VIX index data as an implied volatility proxy

## Feature Engineering
- Log returns
- 20-day annualized realized volatility
- Volatility-of-volatility
- Rolling drawdowns and trend indicators

## Volatility Regime Detection
Two regime detection approaches are implemented and compared:
1. Quantile-based volatility regimes derived from realized volatility thresholds
2. Hidden Markov Model (HMM) to infer latent market volatility states

Each trading day is classified into low, medium, or high volatility regimes.

## Strategy Design
- Underlying asset: SPY
- Strategy structure: Short strangle (out-of-the-money call and put)
- Option pricing: Black–Scholes European option pricing model
- Time to expiration: Approximately 30 days
- Trade entry: Initiated only during high-volatility regimes
- Exit rules:
  - Profit target
  - Stop-loss
  - Time-based exit
  - Volatility regime transition exit

Systematic position sizing and portfolio-level risk controls are applied.

## Risk Analysis
- Monte Carlo simulations under multiple return distribution assumptions
- Stress testing during volatility spikes
- Sensitivity analysis across key strategy parameters
- Evaluation of model risk and assumption breakdowns

## Performance Evaluation
The regime-filtered strategy is evaluated against:
- An identical options strategy without regime filtering
- Buy-and-hold SPY returns for contextual comparison

Performance metrics include CAGR, Sharpe and Sortino ratios, maximum drawdown, and tail-risk measures.

## Project Structure
volatility-regime-options-strategy/
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_regime_detection.ipynb
│ ├── 03_strategy_backtest.ipynb
│ └── 04_robustness_analysis.ipynb
├── src/
│ ├── data_loader.py
│ ├── features.py
│ ├── regimes.py
│ ├── black_scholes.py
│ ├── strategy.py
│ ├── portfolio.py
│ ├── metrics.py
│ └── utils.py
├── reports/
│ ├── paper.pdf
│ └── figures/
├── results/
│ └── backtest_outputs.csv
├── requirements.txt
└── README.md

## Installation and Usage
1. Clone the repository:
git clone https://github.com/sr1565/volatility-regime-options-strategy.git
cd volatility-regime-options-strategy

2. Install dependencies:
pip install -r requirements.txt

3. Run the Jupyter notebooks in numerical order to reproduce the analysis and results.

## Key Assumptions and Limitations
- Options are synthetically priced using the Black–Scholes model
- Volatility smile and skew are not explicitly modeled
- Transaction costs and slippage are simplified
- Results are intended for academic and educational purposes only

## Disclaimer
This project is for academic and educational use only and does not constitute financial advice or a recommendation to trade securities.

## Author
Sherzod Ravshanov

