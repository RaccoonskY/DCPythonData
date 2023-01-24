import unittest

def factorize(x:int):
    pass

class TestFactorize(unittest.TestCase):
    #поместите вашу реализацию класс TestFactorize здесь

    def test_wrong_types_raise_exception(self):
        for x in 'string', 1.5:
            with self.subTest(x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in -1, -10, -100:
            with self.subTest(x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        for x in 0, 1:
            with self.subTest(x):
                self.assertEqual(factorize(x), tuple([x]))

    def test_simple_numbers(self):
        for x in 3, 13, 29:
            with self.subTest(x):
                self.assertEqual(factorize(x), tuple([x]))

    def test_two_simple_multipliers(self):
        for x in 6, 26, 121:
            with self.subTest(x):
                self.assertEqual(len(factorize(x)), 2)

    def test_many_multipliers(self):
        for x in 1001, 9690:
            with self.subTest(x):
                self.assertTrue(len(factorize(x)) > 2)




