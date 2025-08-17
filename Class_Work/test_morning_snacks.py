import unittest
import morning_snacks

class TestForGetSquare(unittest.TestCase):
    def test_that_get_square_function_exists(self):
        result = morning_snacks.get_square([1, 2, 3])
        self.assertIsNotNone(result)

    def test_that_get_square_function_returns_correct_result(self):
        square = morning_snacks.get_square([1, 2, 3, 4, 5])
        self.assertEqual(square, [1, 4, 9, 16, 25])

    def test_that_get_square_handles_empty_list(self):
        square = morning_snacks.get_square([])
        self.assertEqual(square, [])

    def test_that_get_square_handles_single_number(self):
        square = morning_snacks.get_square([7])
        self.assertEqual(square, [49])

    def test_that_get_square_handles_negative_numbers(self):
        square = morning_snacks.get_square([-1, -2, -3])
        self.assertEqual(square, [1, 4, 9])

    def test_that_get_square_handles_zero(self):
        square = morning_snacks.get_square([0])
        self.assertEqual(square, [0])



class TestForStringToLengthOfStringConverter(unittest.TestCase):
    def test_that_words_to_length_function_exists(self):
        converted = morning_snacks.words_to_lengths(["apple", "banana", "cherry"])
        self.assertIsNotNone(converted)

    def test_that_words_to_length_function_returns_correct_result(self):
        converted = morning_snacks.words_to_lengths(["apple", "banana", "cherry"])
        self.assertEqual(converted, [5, 6, 6])

    def test_that_words_to_length_handles_empty_list(self):
        converted = morning_snacks.words_to_lengths([])
        self.assertEqual(converted, [])

    def test_that_words_to_length_handles_single_word(self):
        converted = morning_snacks.words_to_lengths(["hello"])
        self.assertEqual(converted, [5])

    def test_that_words_to_length_handles_words_with_spaces(self):
        converted = morning_snacks.words_to_lengths(["ice cream", "banana"])
        self.assertEqual(converted, [9, 6])

    def test_that_words_to_length_handles_words_with_special_characters(self):
        converted = morning_snacks.words_to_lengths(["hi!", "@world"])
        self.assertEqual(converted, [3, 6])




class TestForEvenNumbersInAList(unittest.TestCase):
    def test_that_is_even_function_exists(self):
        result = morning_snacks.is_Even([1, 2, 3, 4, 5, 6])
        self.assertIsNotNone(result)

    def test_that_is_even_returns_correct_result(self):
        result = morning_snacks.is_Even([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [2, 4, 6])

    def test_that_is_even_returns_empty_list_for_no_even_numbers(self):
        result = morning_snacks.is_Even([1, 3, 5, 7])
        self.assertEqual(result, [])

    def test_that_is_even_returns_all_numbers_if_all_even(self):
        result = morning_snacks.is_Even([2, 4, 6, 8])
        self.assertEqual(result, [2, 4, 6, 8])

    def test_that_is_even_handles_empty_list(self):
        result = morning_snacks.is_Even([])
        self.assertEqual(result, [])



    
class TestFilterShortWords(unittest.TestCase):
    def test_function_exists(self):
        result = morning_snacks.filter_short_words(["apple", "banana", "kiwi", "grapes", "cherry"])
        self.assertIsNotNone(result)

    def test_correct_result_with_sample(self):
        sample_words = ["apple", "banana", "kiwi", "grapes", "cherry"]
        result = morning_snacks.filter_short_words(sample_words)
        self.assertEqual(result, ["apple", "kiwi"])

    def test_handles_empty_list(self):
        result = morning_snacks.filter_short_words([])
        self.assertEqual(result, [])

    


        
