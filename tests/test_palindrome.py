import unittest
from src.palindrome import est_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("Esope reste ici et se repose"))
        self.assertFalse(est_palindrome("Bonjour"))
        self.assertTrue(est_palindrome("12321"))
        self.assertFalse(est_palindrome("Python"))

if __name__ == '__main__':
    unittest.main()
