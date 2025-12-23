import pandas as pd
import yfinance as yf


def load_price_data(ticker, start_date, end_date):
    """
    Download adjusted close price data for a given ticker.
    """
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)

    if data.empty:
        raise ValueError("No data returned. Check ticker or date range.")

    data = data[["Adj Close"]].rename(columns={"Adj Close": "price"})
    data.dropna(inplace=True)

    return data


def load_vix_data(start_date, end_date):
    """
    Download VIX index data for implied volatility comparison.
    """
    vix = yf.download("^VIX", start=start_date, end=end_date, progress=False)

    if vix.empty:
        raise ValueError("No VIX data returned.")

    vix = vix[["Adj Close"]].rename(columns={"Adj Close": "vix"})
    vix.dropna(inplace=True)

    return vix


def merge_datasets(price_data, vix_data=None):
    """
    Merge price data with optional VIX data.
    """
    if vix_data is not None:
        data = price_data.join(vix_data, how="left")
    else:
        data = price_data.copy()

    return data
