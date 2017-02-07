import unittest
from primes import FindPrime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(FindPrime(5))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(FindPrime(index), msg='{} should not be determined to be prime'.format(index))

    def test_is_four_prime(self):
        """Is four successfully determined to be prime?"""
        self.assertFalse(FindPrime(4))

    def test_is_seven_prime(self):
        """Is seven successfully determined to be prime?"""
        self.assertTrue(FindPrime(7))

    def test_is_eightynine_prime(self):
        """Is four successfully determined to be prime?"""
        self.assertTrue(FindPrime(89))

    def test_is_fiftyfour_prime(self):
        """Is four successfully determined to be prime?"""
        self.assertFalse(FindPrime(54))

    def test_is_eightynine_prime(self):
        """Is eighty nine successfully determined to be prime?"""
        self.assertTrue(FindPrime(89))

    def test_is_sixtyseven_prime(self):
        """Is sixty seven successfully determined to be prime?"""
        self.assertTrue(FindPrime(67))

    def test_is_thirtyfive_prime(self):
        """Is thirty five successfully determined to be prime?"""
        self.assertFalse(FindPrime(35))

    def test_is_seventy_prime(self):
        """Is seventy successfully determined to be prime?"""
        self.assertFalse(FindPrime(70))

    def test_is_ninetynine_prime(self):
        """Is ninety nine successfully determined to be prime?"""
        self.assertFalse(FindPrime(99))


if __name__ == '__main__':
    unittest.main()