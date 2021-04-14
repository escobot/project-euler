import unittest
from p005 import solution, modular_sum


class MyTestCase(unittest.TestCase):

    def test_modular_sum_of_2520_between_1_and_10(self):
        self.assertEqual(modular_sum(2520, 10), 0)

    def test_solution_zero(self):
        self.assertEqual(solution(0), 0)

    def test_solution_example(self):
        self.assertEqual(solution(10), 2520)

    def test_solution_answer(self):
        self.assertEqual(solution(20), 232792560)


if __name__ == '__main__':
    unittest.main()
