import unittest
from main import fizzbuzz  

class TestFizzBuzz(unittest.TestCase):

    def test_multiple_de_3(self):
        self.assertEqual(fizzbuzz(100)[5], "fizz")
        self.assertEqual(fizzbuzz(100)[68], "Fizz")

    def test_contient_3(self):
        self.assertEqual(fizzbuzz(100)[22], "Fizz")
        self.assertEqual(fizzbuzz(100)[30], "Fizz") 

    def test_multiple_de_5(self):
        self.assertEqual(fizzbuzz(100)[9], "Buzz")
        self.assertEqual(fizzbuzz(100)[69], "Buzz")

    def test_contient_5(self):
        self.assertEqual(fizzbuzz(100)[51], "Buzz")
        self.assertEqual(fizzbuzz(100)[55], "Buzz")

    def test_multiple_de_3_et_5(self):
        self.assertEqual(fizzbuzz(100)[50], "FizzBuzz")
        self.assertEqual(fizzbuzz(100)[56], "FizzBuzz")

    def test_non_multiple(self):
        self.assertEqual(fizzbuzz(100)[0], "1")
        self.assertEqual(fizzbuzz(100)[43], "44")
        self.assertEqual(fizzbuzz(100)[70], "71")

    def test_multiple_de_3_et_contient_3(self):
        self.assertEqual(fizzbuzz(100)[32], "FizzFizz")
        self.assertEqual(fizzbuzz(100)[38], "FizzFizz")

    def test_multiple_de_5_et_contient_5(self):
        self.assertEqual(fizzbuzz(100)[49], "BuzzBuzz")
        self.assertEqual(fizzbuzz(100)[64], "BuzzBuzz")

    def test_multiple_de_3_de_5_et_contient_3(self):
        self.assertEqual(fizzbuzz(100)[29], "FizzFizzBuzz")

    def test_multiple_de_3_de_5_et_contient_5(self):
        self.assertEqual(fizzbuzz(100)[74], "FizzBuzzBuzz")
        self.assertEqual(fizzbuzz(100)[44], "FizzBuzzBuzz")


if __name__ == '__main__':
    unittest.main()
