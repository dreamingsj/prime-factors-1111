from unittest import TestCase

from prime_factors import Prime


class TestPrime(TestCase):
    def testPrimeFactor(self):
        prime = Prime()
        testcases = [
            (1, None),
            (2, 2),
            (3, 3)
        ]