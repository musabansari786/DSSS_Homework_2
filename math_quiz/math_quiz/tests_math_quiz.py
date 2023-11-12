import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        operators = {'+', '-', '*'}
        for _ in range(1000):
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_calculate_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 5, '*', '10 * 5', 50),
            (8, 3, '-', '8 - 3', 5),
            (3, 0, '+', '3 + 0', 3),  # Test with zero
            (1, 1, '*', '1 * 1', 1),  # Test with one
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = calculate_result(num1, num2, operator)
            expected_result = (expected_problem, expected_answer)
            self.assertEqual((problem, result), expected_result)

if __name__ == "__main__":
    unittest.main()
