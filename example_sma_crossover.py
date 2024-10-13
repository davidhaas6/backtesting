"""example_sma_crossover.py
Example Strategy Implementation: Simple Moving Average Crossover Strategy.
"""

from backtesting_lib import Backtest, Strategy, SMA, CSVDataFeed, Analytics, Visualization, YahooDataFeed
import pandas as pd

class SMACrossoverStrategy(Strategy):
    def init(self):
        self.sma_short = self.indicator(SMA, period=10)
        self.sma_long = self.indicator(SMA, period=50)

    def next(self):
        if self.current_index < len(self.data):
            sma_short = self.sma_short.iloc[self.current_index]
            sma_long = self.sma_long.iloc[self.current_index]
            # Check for NaN values
            if pd.notna(sma_short) and pd.notna(sma_long):
                if sma_short > sma_long and self.broker.position == 0:
                    self.buy()
                elif sma_short < sma_long and self.broker.position > 0:
                    self.sell()

# Load data
data_feed = YahooDataFeed('QTEC', '2010-01-04', '2020-01-01')
data = data_feed.get_data()

# Set up backtest
bt = Backtest(
    data=data,
    strategy=SMACrossoverStrategy,
    cash=10000,
    commission=0.001,
)

# Run backtest
results = bt.run()

# Analyze results
analytics = Analytics(results['Portfolio Value'])
metrics = analytics.calculate_metrics()
analytics.print_metrics()

# Visualize results
# visualization = Visualization(bt)
# visualization.plot_equity_curve()
# visualization.plot_drawdowns()
