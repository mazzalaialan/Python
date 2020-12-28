# -*- coding: utf-8 -*-
import unittest

def prime_factors(numero):
    if numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        return numero * prime_factors(numero-1)


class PrimeFactorsTestCase(unittest.TestCase):

    def test_prime_factors_of_1(self):
        result = prime_factors(1)
        self.assertEqual([],result)

    def test_prime_factors_of_2(self):
        result = prime_factors(2)
        self.assertEqual([2],result)

    def test_prime_factors_of_4(self):
        result = prime_factors(4)
        self.assertEqual([2,2],result)

    def test_prime_factors_of_6(self):
        result = prime_factors(6)
        self.assertEqual([2,3],result)

    def test_prime_factors_of_12(self):
        result = prime_factors(12)
        self.assertEqual([2,2,3],result)

    def test_prime_factors_of_91(self):
        result = prime_factors(91)
        self.assertEqual([2],len(result))
        self.assertIn(7,result)
        self.assertIn(13,result)

if __name__ == '__main__':
    unittest.main()
