import unittest
from src.fizzbuzz import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def setUp(self):
        pass

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz", Fizzbuzz(3))
    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("Buzz", Fizzbuzz(5))
    def test_fizzbuzz__15_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", Fizzbuzz(15))
    def test_fizzbuzz__4_returns_string(self):
        self.assertEqual("4",Fizzbuzz(4))
    # def test_fizzbuzz__9_returns_fizz(self):
    #     self.assertEqual("Fizz", Fizzbuzz(9))
        