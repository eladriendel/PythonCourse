import unittest
import portfolio

class PortfolioTesting(unittest.TestCase):

    # Test adding and withdrawing cash
    def test_cash(self):
        testPortfolio = portfolio.Portfolio()
        testPortfolio.addCash(1000)
        testPortfolio.withdrawCash(750)
        self.assertEqual(250, testPortfolio.cash)

    # Test buying stocks
    def test_buystock(self):
        testPortfolio = portfolio.Portfolio()
        thy = portfolio.Stock(10, "THYAO")
        testPortfolio.buyStock(23, thy)
        amount = testPortfolio.stocks["THYAO"]
        self.assertEqual(amount, 23)
        self.assertEqual(-230, testPortfolio.cash)

    # Test selling stocks
    def test_sellstock(self):
        testPortfolio = portfolio.Portfolio()
        thy = portfolio.Stock(10, "THYAO")
        testPortfolio.buyStock(23, thy)
        testPortfolio.sellStock("THYAO", 18)
        amount = testPortfolio.stocks["THYAO"]
        self.assertEqual(amount, 5)

    # Test buying and selling mutual funds
    def test_MutualFund(self):
        testPortfolio = portfolio.Portfolio()
        abece = portfolio.MutualFund("ABC")
        testPortfolio.buyMutualFund(81.8, abece)
        testPortfolio.sellMutualFund("ABC", 80.8)
        amount = testPortfolio.mutualfunds["ABC"]
        self.assertEqual(amount, 1)


if __name__ == "__main__":
    unittest.main()
