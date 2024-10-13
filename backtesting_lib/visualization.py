"""visualization.py
Visualization Module: Generates charts and visual representations.
"""

import matplotlib.pyplot as plt

class Visualization:
    """Generates charts for backtest results."""
    def __init__(self, backtest):
        self.backtest = backtest

    def plot_equity_curve(self):
        """Plots the equity curve."""
        if hasattr(self.backtest, 'results'):
            plt.figure(figsize=(12, 6))
            self.backtest.results['Portfolio Value'].plot(title='Equity Curve')
            plt.xlabel('Date')
            plt.ylabel('Portfolio Value')
            plt.show()
        else:
            print("No results to plot. Please run the backtest first.")

    def plot_drawdowns(self):
        """Plots the drawdowns."""
        if hasattr(self.backtest, 'results'):
            cumulative_return = self.backtest.results['Portfolio Value'] / self.backtest.results['Portfolio Value'].iloc[0]
            running_max = cumulative_return.cummax()
            drawdown = (cumulative_return - running_max) / running_max
            plt.figure(figsize=(12, 6))
            drawdown.plot(title='Drawdowns')
            plt.xlabel('Date')
            plt.ylabel('Drawdown')
            plt.show()
        else:
            print("No results to plot. Please run the backtest first.")
