import unittest
from src.fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def setUp(self):
        pass

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz", Fizzbuzz(3))
    # def test_fizzbuzz__5_returns_buzz(self):
    #     pass
    # def test_fizzbuzz__3_returns_fizzbuzz(self):
    #     pass