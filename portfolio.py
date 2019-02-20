from random import uniform
from datetime import datetime

# Contains all traded stocks to determine market price
stockMarket = {}

# To record all transactions
class Transaction():
    def __init__(self, kind, trade, amount, ticker = None, price = None, date = datetime.now()):
        self.kind = kind
        self.trade = trade
        self.amount = amount
        self.ticker = ticker
        self.price = price
        self.date = date

# Objects for traded financial instruments
class Stock():
    def __init__(self, price, ticker):
        self.price = price
        self.ticker = ticker
        stockMarket[ticker] = price

class MutualFund():
    def __init__(self, ticker):
        self.price = 1
        self.ticker = ticker

# Client's Portfolio
class Portfolio(object):

    # Starting cash balance, stock and mutual fund dictionaries to keep inventory and transaction list
    cash = 0
    stocks = {}
    mutualfunds = {}
    transactions = []

    # Portfolio operations
    def addCash(self, cash):
        self.cash = self.cash + cash
        # Store in transactions list
        transaction = Transaction("Cash", "Add", cash)
        self.transactions.append(transaction)

    def withdrawCash(self, cash):
        self.cash = self.cash - cash
        # Store in transactions list
        transaction = Transaction("Cash", "Withdraw", cash)
        self.transactions.append(transaction)

    def buyStock(self, amount, stock):
        ticker = stock.ticker
        price = stock.price
        self.stocks[ticker] = amount
        self.cash = self.cash - amount * price
        # Store in transactions list
        transaction = Transaction("Stock", "Buy", amount, ticker, price)
        self.transactions.append(transaction)

    def sellStock(self, ticker, amount):
        price = stockMarket[ticker]
        if ticker in self.stocks.keys():
            # Check if particular stock is owned
            if amount < self.stocks[ticker]:
                self.stocks[ticker] = self.stocks[ticker] - amount
                # Sales price is determined by uniform random distribution based on buy price
                salesPrice = uniform(stockMarket[ticker] * 0.5, stockMarket[ticker] * 1.5)
                self.cash = self.cash + amount * salesPrice
                # Store in transactions list
                transaction = Transaction("Stock", "Sell", amount, ticker, salesPrice)
                self.transactions.append(transaction)
            elif amount == self.stocks[ticker]:
                self.stocks[ticker] = self.stocks[ticker] - amount
                # Sales price is determined by uniform random distribution based on buy price
                salesPrice = uniform(stockMarket[ticker] * 0.5, stockMarket[ticker] * 1.5)
                self.cash = self.cash + amount * salesPrice
                # Remove the stock from stocks dictionary as there is none left
                self.stocks.pop(ticker, None)
                # Store in transactions list
                transaction = Transaction("Stock", "Sell", amount, ticker, salesPrice)
                self.transactions.append(transaction)
            else:
                # Insufficient stocks to sell
                print("You don't have enough stocks called '" + ticker + "'")
        else:
            # No such stock owned
            print("You don't have any stocks called '" + ticker + "'")

    def buyMutualFund(self, amount, mutualfund):
        ticker = mutualfund.ticker
        self.mutualfunds[ticker] = amount
        # Price is set to $1
        self.cash = self.cash - amount * 1
        # Store in transactions list
        transaction = Transaction("Mutual Fund", "Buy", amount, ticker, 1)
        self.transactions.append(transaction)

    def sellMutualFund(self, ticker, amount):
        if ticker in self.mutualfunds.keys():
            # Check if a share of particular mutual fund is owned
            if amount < self.mutualfunds[ticker]:
                self.mutualfunds[ticker] = self.mutualfunds[ticker] - amount
                # Sales price is determined by uniform random distribution
                salesPrice = uniform(0.9, 1.2)
                self.cash = self.cash + amount * salesPrice
                # Store in transactions list
                transaction = Transaction("Mutual Fund", "Sell", amount, ticker, salesPrice)
                self.transactions.append(transaction)
            elif amount == self.mutualfunds[ticker]:
                self.mutualfunds[ticker] = self.mutualfunds[ticker] - amount
                # Sales price is determined by uniform random distribution
                salesPrice = uniform(0.9, 1.2)
                self.cash = self.cash + amount * salesPrice
                # Remove the mutual fund from mutualfunds dictionary as there is none left
                self.mutualfunds.pop(ticker, None)
                # Store in transactions list
                transaction = Transaction("Mutual Fund", "Sell", amount, ticker, salesPrice)
                self.transactions.append(transaction)
            else:
                # Insufficient mutual fund shares to sell
                print("You don't have enough mutual fund shares called '" + ticker + "'")
        else:
            # No shares of such mutual fund owned
            print("You don't possess any mutual fund shares called '" + ticker + "'")

    # To print portfolio
    def __str__(self):
        stocks = self.stocks.keys()
        mutualfunds = self.mutualfunds.keys()
        show = []
        show.append("Your Cash Balance: $" + str(self.cash))
        for stocks in stocks:
            show.append("Stocks: You Have " + str(self.stocks[stocks]) + " Shares of " + str(stocks))
        for mutualfund in mutualfunds:
            show.append("Mutual Funds: You Have " + str(self.mutualfunds[mutualfund]) + " Shares of " + str(mutualfund))
        return "\n".join(show)

    # To print transaction history
    def history(self):
        show = ["---------- Date ---------- Kind - Trade - Amount - Ticker - Price -"]
        for transaction in self.transactions:
            kind = transaction.kind
            trade = transaction.trade
            amount = transaction.amount
            ticker = transaction.ticker
            price = transaction.price
            date = transaction.date
            show.append(str(date) + " " + str(kind) + " " + str(trade) + " " + str(amount) + " " + str(ticker) + " " + str(price))
        result = "\n".join(show)
        print(result)
