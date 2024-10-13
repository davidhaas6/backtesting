# Backtesting Library

A simple and intuitive Python library for backtesting algorithmic trading strategies.

NOTE: ** Most of this project is AI-generated **

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Examples](#examples)
  - [SMA Crossover Strategy](#sma-crossover-strategy)
  - [RSI Mean Reversion Strategy](#rsi-mean-reversion-strategy)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Backtesting Library provides a straightforward framework for developing, testing, and analyzing trading strategies using historical data. Designed for ease of use and flexibility, it allows users to implement strategies quickly and evaluate their performance before deploying them in live markets.

## Features

- **Simple API**: Easy-to-understand classes and methods for strategy development.
- **Technical Indicators**: Built-in indicators like SMA, EMA, RSI, and the ability to add custom indicators.
- **Execution Simulation**: Simulates order execution with customizable commission and slippage.
- **Performance Analytics**: Calculates key performance metrics such as total return, volatility, Sharpe ratio, and maximum drawdown.
- **Visualization**: Generates charts for equity curves and drawdowns.
- **Extensible**: Modular design allows for easy addition of new features and indicators.

## Installation

To use the Backtesting Library, clone the repository and ensure you have the required dependencies:

```bash
git clone https://github.com/yourusername/backtesting-lib.git
cd backtesting-lib
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Quick Start

Here's how to get started with the Backtesting Library:

1. **Load your data**: Ensure your historical data is in CSV format with at least 'Date' and 'Close' columns.

2. **Define a strategy**: Subclass the `Strategy` class and implement the `init()` and `next()` methods.

3. **Run a backtest**: Use the `Backtest` class to run your strategy over the data.

4. **Analyze and visualize results**: Use the `Analytics` and `Visualization` modules.

```python
from backtesting_lib import Backtest, Strategy, SMA, CSVDataFeed, Analytics, Visualization

# Step 1: Load data
data_feed = CSVDataFeed('your_data.csv')
data = data_feed.get_data()

# Step 2: Define a strategy
class MyStrategy(Strategy):
    def init(self):
        self.sma_short = SMA(self.data, period=10).values
        self.sma_long = SMA(self.data, period=50).values

    def next(self):
        idx = self.current_index
        if self.sma_short.iloc[idx] > self.sma_long.iloc[idx]:
            if self.broker.position == 0:
                self.buy()
        elif self.sma_short.iloc[idx] < self.sma_long.iloc[idx]:
            if self.broker.position > 0:
                self.sell()

# Step 3: Run a backtest
bt = Backtest(data=data, strategy=MyStrategy, cash=10000, commission=0.001)
results = bt.run()

# Step 4: Analyze and visualize results
analytics = Analytics(results['Portfolio Value'])
analytics.calculate_metrics()
analytics.print_metrics()

visualization = Visualization(bt)
visualization.plot_equity_curve()
visualization.plot_drawdowns()
```

## Examples

### SMA Crossover Strategy

Implements a simple moving average crossover strategy.

```python
from backtesting_lib import Backtest, Strategy, SMA

class SMACrossoverStrategy(Strategy):
    def init(self):
        self.sma_short = SMA(self.data, period=10).values
        self.sma_long = SMA(self.data, period=50).values

    def next(self):
        idx = self.current_index
        sma_short = self.sma_short.iloc[idx]
        sma_long = self.sma_long.iloc[idx]

        if sma_short > sma_long and self.broker.position == 0:
            self.buy()
        elif sma_short < sma_long and self.broker.position > 0:
            self.sell()
```

### RSI Mean Reversion Strategy

Uses the Relative Strength Index to identify overbought and oversold conditions.

```python
from backtesting_lib import Backtest, Strategy, RSI

class RSIMeanReversionStrategy(Strategy):
    def init(self):
        self.rsi = RSI(self.data, period=14).values
        self.upper_threshold = 70
        self.lower_threshold = 30

    def next(self):
        idx = self.current_index
        rsi_value = self.rsi.iloc[idx]

        if rsi_value < self.lower_threshold and self.broker.position == 0:
            self.buy()
        elif rsi_value > self.upper_threshold and self.broker.position > 0:
            self.sell()
```

## Documentation

For detailed documentation and API reference, please refer to the `docs/` directory.

The main modules include:

- **Data Module**: `data.py` - Handles data loading and preprocessing.
- **Indicator Module**: `indicators.py` - Provides built-in technical indicators.
- **Strategy Module**: `strategy.py` - Base class for defining strategies.
- **Execution Engine**: `execution.py` - Simulates order execution.
- **Backtesting Engine**: `backtest.py` - Runs the strategy over historical data.
- **Analytics Module**: `analytics.py` - Calculates performance metrics.
- **Visualization Module**: `visualization.py` - Generates performance charts.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write tests for your changes.
4. Submit a pull request with a detailed description of your changes.

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This library is for educational purposes only. Trading involves risk, and past performance is not indicative of future results. Use this library at your own risk.