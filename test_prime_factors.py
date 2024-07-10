from unittest import TestCase

from prime_factors import Prime


class TestPrime(TestCase):
    def setUp(self):
        self.prime = Prime()

    def testPrimeFactor(self):
        testcases = [
            (1, []),
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (5, [5]),
            (6, [2, 3])
        ]

        for case in testcases:
            number, answer = case
            with self.subTest(f'PRIME FACTORS OF {number}'):
                self.assertEqual(answer, self.prime.of(number))
