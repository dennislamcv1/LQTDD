import unittest
from .tested_functions import adder


class TestAdder(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3, 5), 8)

    def test_adds_negative_numbers_correctly(self):
        self.fail("This test has not yet been written!")

    def test_adds_numbers_to_zero_correctly(self):
        self.fail("This test has not yet been written!")

    def test_adds_three_integers_correctly(self):
        self.fail("This test has not yet been written!")

    def test_adds_forty_integers_correctly(self):
        self.fail("This test has not yet been written!")

    def test_raises_an_exception_when_given_one_argument(self):
        self.fail("This test has not yet been written!")

    def test_raises_an_exception_on_string_arguments(self):
        self.fail("This test has not yet been written!")