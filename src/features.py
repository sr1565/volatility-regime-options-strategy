import numpy as np
import pandas as pd


def compute_log_returns(df):
    """
    Compute daily log returns.
    """
    df = df.copy()
    df["log_return"] = np.log(df["price"] / df["price"].shift(1))
    return df


def compute_realized_volatility(df, window=20, trading_days=252):
    """
    Compute rolling annualized realized volatility.
    """
    df = df.copy()
    df["realized_vol"] = (
        df["log_return"].rolling(window).std() * np.sqrt(trading_days)
    )
    return df


def compute_vol_of_vol(df, window=20):
    """
    Compute volatility of realized volatility.
    """
    df = df.copy()
    df["vol_of_vol"] = df["realized_vol"].rolling(window).std()
    return df


def compute_drawdown(df):
    """
    Compute rolling drawdown from peak price.
    """
    df = df.copy()
    cumulative_max = df["price"].cummax()
    df["drawdown"] = (df["price"] - cumulative_max) / cumulative_max
    return df


def compute_trend_indicators(df, short_window=50, long_window=200):
    """
    Compute moving average trend indicators.
    """
    df = df.copy()
    df["ma_short"] = df["price"].rolling(short_window).mean()
    df["ma_long"] = df["price"].rolling(long_window).mean()
    df["trend"] = df["ma_short"] - df["ma_long"]
    return df


def build_features(df):
    """
    Build full feature set for modeling and strategy.
    """
    df = compute_log_returns(df)
    df = compute_realized_volatility(df)
    df = compute_vol_of_vol(df)
    df = compute_drawdown(df)
    df = compute_trend_indicators(df)
    df.dropna(inplace=True)
    return df
