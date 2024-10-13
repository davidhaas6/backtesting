"""analytics.py
Analytics Module: Provides performance metrics and reporting.
"""

import pandas as pd
import numpy as np

class Analytics:
    """Calculates performance metrics."""
    def __init__(self, portfolio_values, trading_days=252):
        self.portfolio_values = portfolio_values
        self.metrics = {}
        self.trading_days = trading_days

    def calculate_metrics(self):
        returns = self.portfolio_values.pct_change().fillna(0)
        total_return = self.portfolio_values.iloc[-1] / self.portfolio_values.iloc[0] - 1
        annualized_return = (1 + total_return) ** (self.trading_days / len(self.portfolio_values)) - 1
        volatility = returns.std() * np.sqrt(self.trading_days)
        if returns.std() != 0:
            sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(self.trading_days)
        else:
            sharpe_ratio = np.nan
        max_drawdown = self.calculate_max_drawdown()
        self.metrics = {
            'Total Return': total_return,
            'Annualized Return': annualized_return,
            'Volatility': volatility,
            'Sharpe Ratio': sharpe_ratio,
            'Max Drawdown': max_drawdown,
        }
        return self.metrics

    def calculate_max_drawdown(self):
        cumulative_return = self.portfolio_values / self.portfolio_values.iloc[0]
        running_max = cumulative_return.cummax()
        drawdown = (cumulative_return - running_max) / running_max
        max_drawdown = drawdown.min()
        return max_drawdown

    def print_metrics(self):
        for key, value in self.metrics.items():
            if pd.notna(value):
                print(f"{key}: {value:.2%}")
            else:
                print(f"{key}: NaN")
