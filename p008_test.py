import unittest
from p008 import solution


class MyTestCase(unittest.TestCase):

    def test_solution_example(self):
        self.assertEqual(solution(4), 5832)

    def test_solution_answer(self):
        self.assertEqual(solution(13), 23514624000)


if __name__ == '__main__':
    unittest.main()
