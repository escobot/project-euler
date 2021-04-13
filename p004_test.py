import unittest
from p004 import solution, is_palindrome


class MyTestCase(unittest.TestCase):

    def test_is_palindrome_zero(self):
        self.assertEqual(is_palindrome("o"), True)

    def test_is_palindrome_positive_even(self):
        self.assertEqual(is_palindrome("osso"), True)

    def test_is_palindrome_positive_odd(self):
        self.assertEqual(is_palindrome("laval"), True)

    def test_is_palindrome_negative_even(self):
        self.assertEqual(is_palindrome("oslo"), False)

    def test_is_palindrome_negative_odd(self):
        self.assertEqual(is_palindrome("lavas"), False)

    def test_solution_zero(self):
        self.assertEqual(solution(0, 0), 0)

    def test_solution_example(self):
        self.assertEqual(solution(10, 99), 9009)

    def test_solution_answer(self):
        self.assertEqual(solution(100, 999), 906609)


if __name__ == '__main__':
    unittest.main()

