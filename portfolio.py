class Portfolio:
    def __init__(self):
        self._stocks = []

    def buy(self, name, str, stock):
        self._stocks.append((name,shares,price))
    
    def cost(self):
        return(
            shares*price for name, shares, price in self._stocks
        ) # generator





