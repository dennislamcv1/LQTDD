import unittest
from .tested_functions import divider


class TestDivider(unittest.TestCase):
    """Requirements to test:
    
        - Returns non-integer results (does not floor divide)
        - Raises ValueError if too many or too few arguments provided (division is binary)
        - Raises TypeError if non-integer arguments provided
        - Raises ValueError if attempting to divide by 0 (treating the error as a bad argument issue, not a math issue)
        - Handles arbitrarily large integer dividends/divisors
        - Can be called multiple times in succession accurately (divider(divider(divider(...
    """

    def test_divides_two_integers_correctly(self):
        self.assertEqual(divider(10, 2), 5)