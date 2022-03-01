class Transaction():
    BUY, SELL = 'buy', 'sell'

    def __init__(self, type, cost, quantity, tax = 0):
        self.type = type
        self.cost = cost
        self.quantity = quantity
        self.tax = tax        

    def __str__(self) -> str:
        return f'type:{self.type} cost:{self.cost} quantity:{self.quantity} tax:{self.tax}'