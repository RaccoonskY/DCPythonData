from fib import fib
import unittest

"""
This is example of using unittest in Py.
tests are based of fibonacci function from fib.py

PS. To have tests we must have class inherited from ut.TestCase
and 'test_' in the beginning of all test methods
"""


class TestFibonacciNumbers(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def test_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib(n), fib_n)

    def test_positive(self):
        self.assertEqual(fib(10), 55)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -1)
        with self.subTest(i=2):
            self.assertRaises(ArithmeticError, fib, -10)

    def test_fractional(self):
        self.assertRaises(ArithmeticError, fib, 2.5)


if __name__ == '__main__':
    # executes the tests
    unittest.main()
