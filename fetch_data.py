import yfinance as yf
import pandas as pd

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start = start_date, end = end_date)['Close']
    return data
