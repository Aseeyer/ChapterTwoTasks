import unittest
import dollar

class TestForDollarAmount(unittest.TestCase):
    def test_that_dollar_exchange_function_exists(self):
        dollar.get_dollar_exchange(20)
    
    def test_that_dollar_exchange_function_returns_correct_function(self):
        convert = dollar.get_dollar_exchange(20)
        self.assertEqual(convert, "₦31,000.00")
 
    def test_that_dollar_exchange_function_raises_validation_with_incorrect_value(self):
        self.assertRaises(ValueError, dollar.get_dollar_exchange, "Emma")

    def test_that_dollar_exchange_function_return_correct_result(self):
        exchange = dollar.get_dollar_exchange(2.5)
        self.assertEqual(exchange, "₦3,875.00")
    def test_that_dollar_exchange_function_raises_validation_with_negative_values(self):
        self.assertRaises(ValueError, dollar.get_dollar_exchange, -25)
        
    def test_that_dollar_exchange_function_return_correct_format(self):
        exchange = dollar.get_dollar_exchange(2.5)
        self.assertEqual(exchange, "₦3,875.00")

