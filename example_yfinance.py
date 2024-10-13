import yfinance as yf
import pandas as pd

# Download data for a single stock (AAPL)
data = yf.download('AAPL', start='2010-01-01', end='2020-01-01')

print(data.head())
