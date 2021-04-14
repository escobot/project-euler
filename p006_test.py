import unittest
from p006 import solution


class MyTestCase(unittest.TestCase):
    def test_solution_zero(self):
        self.assertEqual(solution(0), 0)

    def test_solution_example(self):
        self.assertEqual(solution(10), 2640)

    def test_solution_answer(self):
        self.assertEqual(solution(100), 25164150)


if __name__ == '__main__':
    unittest.main()
