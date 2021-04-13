import unittest
from p002 import solution


class MyTestCase(unittest.TestCase):

    def test_solution_zero(self):
        self.assertEqual(solution(0), 0)

    def test_solution_example(self):
        self.assertEqual(solution(10), 10)

    def test_solution_answer(self):
        self.assertEqual(solution(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
