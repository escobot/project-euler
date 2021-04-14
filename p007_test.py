import unittest
from p007 import solution


class MyTestCase(unittest.TestCase):
    def test_solution_zero(self):
        self.assertEqual(solution(0), 1)

    def test_solution_example(self):
        self.assertEqual(solution(6), 13)

    def test_solution_answer(self):
        self.assertEqual(solution(10001), 104743)

    def test_solution_answer(self):
        self.assertEqual(solution(10001), 104743)


if __name__ == '__main__':
    unittest.main()
