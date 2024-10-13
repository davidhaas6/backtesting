"""execution.py
Execution Engine: Simulates order execution and portfolio management.
"""

class Broker:
    """Simulates order handling and portfolio management."""
    def __init__(self, cash, commission=0.0, slippage=0.0):
        self.cash = cash
        self.commission = commission
        self.slippage = slippage
        self.position = 0
        self.history = []

    def buy(self, price, amount=None, date=None):
        """Executes a buy order."""
        adjusted_price = price + self.slippage
        total_cost_per_unit = adjusted_price * (1 + self.commission)
        if amount is None:
            amount = int(self.cash // total_cost_per_unit)
            if amount <= 0:
                return  # Not enough cash to buy any shares
        cost = total_cost_per_unit * amount
        if self.cash >= cost:
            self.cash -= cost
            self.position += amount
            self.history.append({
                'action': 'buy',
                'price': adjusted_price,
                'amount': amount,
                'date': date
            })

    def sell(self, price, amount=None, date=None):
        """Executes a sell order."""
        adjusted_price = price - self.slippage
        total_revenue_per_unit = adjusted_price * (1 - self.commission)
        if amount is None:
            amount = self.position
            if amount <= 0:
                return  # No shares to sell
        if self.position >= amount:
            revenue = total_revenue_per_unit * amount
            self.cash += revenue
            self.position -= amount
            self.history.append({
                'action': 'sell',
                'price': adjusted_price,
                'amount': amount,
                'date': date
            })

    def get_portfolio_value(self, current_price):
        """Calculates total portfolio value."""
        return self.cash + self.position * current_price

    def get_positions(self):
        """Returns current positions."""
        return {'cash': self.cash, 'position': self.position}
