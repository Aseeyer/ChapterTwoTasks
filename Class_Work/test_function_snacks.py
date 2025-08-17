import unittest
import function_snacks

class TestForDivideOrSquareRoot(unittest.TestCase):
    def test_that_divide_or_square_function_exists(self):
        function_snacks.divide_or_square(10)

    def test_that_divide_or_square_function_returns_correct_value(self):
        operation = function_snacks.divide_or_square(15)
        self.assertEqual(operation, 3.87)

    def test_that_divide_or_square_function_raises_validation_with_negative_values(self):
        self.assertRaises(ValueError, function_snacks.divide_or_square, -25)

    def test_that_divide_or_square_function_raise_validation_with_incorrect_value(self):
        self.assertRaises(ValueError,function_snacks.divide_or_square, "EzeEmma" )

    def test_that_divide_or_square_function_raise_validation_with_decimal(self):
        self.assertRaises(ValueError,function_snacks.divide_or_square, 4.5 )


class TestForFutureInvestment(unittest.TestCase):
    def test_that_future_investment_function_exists(self):
        function_snacks.get_future_investment(400, 19, 2)

    def test_that_future_investment_function_returns_correct_result(self):
        invest = function_snacks.get_future_investment(400, 1, 2)
        self.assertAlmostEqual(invest, 6710886400)

    def test_that_future_investment_function_raises_validation_with_negative_values(self):
        self.assertRaises(ValueError, function_snacks.get_future_investment, -400, -1, -2)

    def test_that_future_investment_function_raises_validation_with_incorrect_values(self):
        self.assertRaises(ValueError, function_snacks.get_future_investment, "a", "b", "c")

    def test_that_future_investment_function_raises_validation_with_decimal(self):
        self.assertRaises(ValueError,function_snacks.get_future_investment, 400.1, 1.1, 2.1 )


class TestForIsFloat(unittest.TestCase):
    def test_that_only_floats_function_exists(self):
        function_snacks.only_floats(1, 2)
    
    def test_that_only_floats_function_returns_correct_value(self):
        result = function_snacks.only_floats(12.3, 23.2)
        self.assertEqual(result, 2)

    def test_that_only_floats_function_raises_validation_with_negative_values(self):
       self.assertRaises(ValueError, function_snacks.only_floats, -12.3, -23.2)

    def test_that_only_floats_function_

    





















