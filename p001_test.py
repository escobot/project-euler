import unittest
from p001 import solution


class MyTestCase(unittest.TestCase):

    def test_solution_zero(self):
        self.assertEqual(solution(0), 0)

    def test_solution_example(self):
        self.assertEqual(solution(10), 23)

    def test_solution_answer(self):
        self.assertEqual(solution(1000), 233168)


if __name__ == '__main__':
    unittest.main()
