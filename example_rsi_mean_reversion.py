"""example_rsi_mean_reversion.py
Example Strategy Implementation: RSI Mean Reversion Strategy.
"""

from backtesting_lib import Backtest, Strategy, RSI, CSVDataFeed, Analytics, Visualization
import pandas as pd
import yfinance

from backtesting_lib.data import YahooDataFeed

class RSIMeanReversionStrategy(Strategy):
    def init(self):
        self.rsi = self.indicator(RSI, period=14)
        self.upper_threshold = 70
        self.lower_threshold = 30

    def next(self):
        if self.current_index < len(self.data):
            rsi_value = self.rsi.iloc[self.current_index]
            # Check for NaN values
            if pd.notna(rsi_value):
                if rsi_value < self.lower_threshold and self.broker.position == 0:
                    self.buy()
                elif rsi_value > self.upper_threshold and self.broker.position > 0:
                    self.sell()

# Load data
data_feed = YahooDataFeed('SPY', '2010-01-04', '2020-01-01')
data = data_feed.get_data()

# Set up backtest
bt = Backtest(
    data=data,
    strategy=RSIMeanReversionStrategy,
    cash=50000,
    commission=0.0005,
)

# Run backtest
results = bt.run()

# Analyze results
analytics = Analytics(results['Portfolio Value'])
metrics = analytics.calculate_metrics()
analytics.print_metrics()

# Visualize results
visualization = Visualization(bt)
visualization.plot_equity_curve()
visualization.plot_drawdowns()
