import unittest
from p010 import solution


class MyTestCase(unittest.TestCase):

    def test_solution_example(self):
        self.assertEqual(solution(10), 17)

    def test_solution_answer(self):
        self.assertEqual(solution(2000000), 142913828922)


if __name__ == '__main__':
    unittest.main()
