"""data.py
Data Module: Handles data ingestion and preprocessing.
"""

import pandas as pd
from abc import ABC, abstractmethod
import yfinance

class DataFeed(ABC):
    """Data Feed Interface: Abstract base class to support multiple data sources."""
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_data(self):
        pass

class CSVDataFeed(DataFeed):
    """Loads data from a CSV file."""
    def __init__(self, file_path, date_column='Date'):
        try:
            self.data = pd.read_csv(
                file_path,
                parse_dates=[date_column],
                index_col=date_column
            )
            self.preprocess()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the CSV file: {e}")

    def preprocess(self):
        """Cleans and preprocesses the data."""
        self.data.sort_index(inplace=True)
        self.data.fillna(method='ffill', inplace=True)
        self.data.fillna(method='bfill', inplace=True)
        # Additional preprocessing steps can be added here.

    def get_data(self):
        """Returns the preprocessed data."""
        return self.data


class YahooDataFeed(DataFeed):
    """Loads data from a CSV file."""
    def __init__(self, ticker, start_date, end_date, date_column='Date'):
        try:
            self.data = yfinance.download(ticker, start=start_date, end=end_date)
            # self.data['Date'] = pd.to_datetime(self.data.index)
            # self.data.set_index('Date', inplace=True)
            # self.data = pd.read_csv(
            #     file_path,
            #     parse_dates=[date_column],
            #     index_col=date_column
            # )
            self.preprocess()
        except Exception as e:
            raise Exception(f"An error occurred while reading the ticker: {e}")

    def preprocess(self):
        """Cleans and preprocesses the data."""
        self.data.sort_index(inplace=True)
        self.data.ffill(inplace=True)
        self.data.bfill(inplace=True)
        # Additional preprocessing steps can be added here.

    def get_data(self):
        """Returns the preprocessed data."""
        return self.data

