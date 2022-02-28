
import unittest
from finance_formulas import Finance


class TestFinances(unittest.TestCase):
    def test_cash_flow(self):
        t1 = Finance()
        self.assertTrue(t1.cash_flow(10000, 5500), 4500)

    def test_net_worth(self):
        pass

    def test_net_income(self):
        pass

    def test_simple_interest(self):
        pass

    def test_gains_or_losses(self):
        pass


if __name__ == '__main__':
    unittest.TestCase()