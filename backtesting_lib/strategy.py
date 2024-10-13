"""strategy.py
Strategy Module: Allows users to define trading strategies.
"""

import pandas as pd

class Strategy:
    """Base Strategy Class for users to define their strategies."""
    def __init__(self, broker, data):
        self.broker = broker
        self.data = data
        self.indicators = {}
        self.current_index = 0
        self.init()

    def init(self):
        """Initialization logic (e.g., setting up indicators)."""
        pass

    def next(self):
        """Defines logic for each time step."""
        raise NotImplementedError("Strategy.next() must be overridden.")

    def indicator(self, indicator_class, *args, **kwargs):
        """Registers and returns an indicator."""
        indicator = indicator_class(self.data, *args, **kwargs)
        self.indicators[indicator.name] = indicator.values
        return indicator.values

    def buy(self, amount=None):
        """Places a buy order."""
        if self.current_index < len(self.data):
            price = self.data['Close'].iloc[self.current_index]
            date = self.data.index[self.current_index]
            self.broker.buy(price, amount, date)
        else:
            pass  # Index out of range, cannot execute buy

    def sell(self, amount=None):
        """Places a sell order."""
        if self.current_index < len(self.data):
            price = self.data['Close'].iloc[self.current_index]
            date = self.data.index[self.current_index]
            self.broker.sell(price, amount, date)
        else:
            pass  # Index out of range, cannot execute sell

    def get_indicator(self, name):
        """Retrieves the current value of an indicator."""
        if name in self.indicators:
            return self.indicators[name].iloc[self.current_index]
        else:
            raise ValueError(f"Indicator '{name}' not found.")
