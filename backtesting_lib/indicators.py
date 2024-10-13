"""indicators.py
Indicator Library: Built-in technical indicators.
"""

import pandas as pd
import numpy as np

class Indicator:
    """Base class for indicators."""
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.values = None
        self.name = ''
        self.calculate()

    def calculate(self):
        """Calculates the indicator."""
        raise NotImplementedError("Indicator.calculate() must be overridden.")

class SMA(Indicator):
    """Simple Moving Average."""
    def __init__(self, data, period):
        self.period = period
        self.name = f'SMA_{period}'
        super().__init__(data)

    def calculate(self):
        self.values = self.data['Close'].rolling(window=self.period).mean()

class RSI(Indicator):
    """Relative Strength Index."""
    def __init__(self, data, period):
        self.period = period
        self.name = f'RSI_{period}'
        super().__init__(data)

    def calculate(self):
        delta = self.data['Close'].diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)
        avg_gain = gain.rolling(window=self.period).mean()
        avg_loss = loss.rolling(window=self.period).mean()
        # Avoid division by zero
        avg_loss = avg_loss.replace(0, np.nan)
        rs = avg_gain / avg_loss
        rs = rs.fillna(0)  # Handle NaN values
        self.values = 100 - (100 / (1 + rs))
