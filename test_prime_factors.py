from unittest import TestCase

from prime_factors import Prime


class TestPrime(TestCase):
    def testPrimeFactor(self):
        prime = Prime()
        testcases = [
            (1, []),
            # (2, [2]),
            # (3, [3])
        ]

        for case in testcases:
            number, answer = case
            with self.subTest(f'PRIME FACTORS OF {number}'):
                self.assertEqual(answer, prime.of(number))
