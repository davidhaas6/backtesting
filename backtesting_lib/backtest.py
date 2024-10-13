"""backtest.py
Backtesting Engine: Runs the strategy over historical data.
"""

import pandas as pd
from .execution import Broker

class Backtest:
    """Runs the strategy over historical data."""
    def __init__(self, data, strategy, cash=10000, commission=0.0, slippage=0.0):
        self.data = data
        self.strategy_class = strategy
        self.cash = cash
        self.commission = commission
        self.slippage = slippage
        self.broker = Broker(cash, commission, slippage)
        self.strategy = self.strategy_class(self.broker, self.data)
        self.portfolio_values = []

    def run(self):
        """Executes the backtest."""
        data_length = len(self.data)
        for idx in range(data_length):
            self.strategy.current_index = idx
            self.strategy.next()
            current_price = self.data['Close'].iloc[idx]
            portfolio_value = self.broker.get_portfolio_value(current_price)
            self.portfolio_values.append(portfolio_value)
        self.results = pd.DataFrame({
            'Portfolio Value': self.portfolio_values
        }, index=self.data.index[:len(self.portfolio_values)])
        return self.results

    def plot(self):
        """Plots the portfolio value over time."""
        if hasattr(self, 'results'):
            self.results['Portfolio Value'].plot(title='Portfolio Value Over Time')
        else:
            print("No results to plot. Please run the backtest first.")
