import unittest
import Weekend2

class TestWeekend2Tasks(unittest.TestCase):

    def test_sum_inner_lists_function_exists(self):
        result = Weekend2.sum_inner_lists([[1, 2], [3, 4]])
        self.assertIsNotNone(result)

    def test_sum_inner_lists_returns_correct_output(self):
        sample = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
        result = Weekend2.sum_inner_lists(sample)
        self.assertEqual(result, [9, 13, 18])

    def test_sum_inner_lists_handles_empty_inner_list(self):
        sample = [[1, 2], [], [3, 4, 5]]
        result = Weekend2.sum_inner_lists(sample)
        self.assertEqual(result, [3, 0, 12])

    def test_sum_columns_function_exists(self):
        result = Weekend2.sum_columns([[1, 2], [3, 4]])
        self.assertIsNotNone(result)

    def test_sum_columns_returns_correct_output(self):
        sample = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
        result = Weekend2.sum_columns(sample)
        self.assertEqual(result, [7, 14, 19])

    def test_sum_columns_handles_empty_outer_list(self):
        sample = []
        result = Weekend2.sum_columns(sample)
        self.assertEqual(result, [])




class TestFilterTasks(unittest.TestCase):

    def test_get_even_numbers_function_exists(self):
        result = Weekend2.get_even_numbers()
        self.assertIsNotNone(result)

    def test_get_even_numbers_returns_correct_output(self):
        result = Weekend2.get_even_numbers()
        self.assertEqual(result, list(range(2, 21, 2)))

    def test_get_even_numbers_output_type(self):
        result = Weekend2.get_even_numbers()
        self.assertIsInstance(result, list)

    def test_words_longer_than_five_function_exists(self):
        result = Weekend2.words_longer_than_five(['cat', 'elephant'])
        self.assertIsNotNone(result)

    def test_words_longer_than_five_returns_correct_output(self):
        words = ['cat', 'elephant', 'tiger', 'lion']
        result = Weekend2.words_longer_than_five(words)
        self.assertEqual(result, ['elephant'])

    def test_words_longer_than_five_empty_input(self):
        result = Weekend2.words_longer_than_five([])
        self.assertEqual(result, [])

    def test_tuples_first_value_gt_two_function_exists(self):
        result = Weekend2.tuples_first_value_gt_two([(1, 'A')])
        self.assertIsNotNone(result)

    def test_tuples_first_value_gt_two_returns_correct_output(self):
        tuples_list = [(1, 'A'), (4, 'B'), (2, 'C')]
        result = Weekend2.tuples_first_value_gt_two(tuples_list)
        self.assertEqual(result, [(4, 'B')])

    def test_tuples_first_value_gt_two_empty_input(self):
        result = Weekend2.tuples_first_value_gt_two([])
        self.assertEqual(result, [])

    def test_divisible_by_three_and_five_function_exists(self):
        result = Weekend2.divisible_by_three_and_five()
        self.assertIsNotNone(result)

    def test_divisible_by_three_and_five_returns_correct_output(self):
        result = Weekend2.divisible_by_three_and_five()
        self.assertEqual(result, [15, 30, 45])

    def test_divisible_by_three_and_five_output_type(self):
        result = Weekend2.divisible_by_three_and_five()
        self.assertIsInstance(result, list)

    def test_filter_palindromes_function_exists(self):
        result = Weekend2.filter_palindromes(['level'])
        self.assertIsNotNone(result)

    def test_filter_palindromes_returns_correct_output(self):
        words = ['level', 'world', 'madam', 'python']
        result = Weekend2.filter_palindromes(words)
        self.assertEqual(result, ['level', 'madam'])

    def test_filter_palindromes_empty_input(self):
        result = Weekend2.filter_palindromes([])
        self.assertEqual(result, [])





class TestMapTasks(unittest.TestCase):

    def test_convert_to_uppercase_function_exists(self):
        result = Weekend2.convert_to_uppercase(['python'])
        self.assertIsNotNone(result)

    def test_convert_to_uppercase_returns_correct_output(self):
        words = ['python', 'java', 'c++']
        result = Weekend2.convert_to_uppercase(words)
        self.assertEqual(result, ['PYTHON', 'JAVA', 'C++'])

    def test_convert_to_uppercase_empty_input(self):
        result = Weekend2.convert_to_uppercase([])
        self.assertEqual(result, [])

    def test_square_numbers_function_exists(self):
        result = Weekend2.square_numbers()
        self.assertIsNotNone(result)

    def test_square_numbers_returns_correct_output(self):
        result = Weekend2.square_numbers()
        self.assertEqual(result, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_square_numbers_output_type(self):
        result = Weekend2.square_numbers()
        self.assertIsInstance(result, list)

    def test_capitalize_names_function_exists(self):
        result = Weekend2.capitalize_names(['john'])
        self.assertIsNotNone(result)

    def test_capitalize_names_returns_correct_output(self):
        names = ['john', 'mary', 'steve']
        result = Weekend2.capitalize_names(names)
        self.assertEqual(result, ['John', 'Mary', 'Steve'])

    def test_capitalize_names_empty_input(self):
        result = Weekend2.capitalize_names([])
        self.assertEqual(result, [])

    def test_add_tax_function_exists(self):
        result = Weekend2.add_tax([100])
        self.assertIsNotNone(result)

    def test_add_tax_returns_correct_output(self):
        prices = [100, 200, 300]
        result = Weekend2.add_tax(prices)
        expected = [110.0, 220.0, 330.0]
        result_rounded = [round(x, 2) for x in result]
        self.assertEqual(result_rounded, expected)


    def test_add_tax_empty_input(self):
        result = Weekend2.add_tax([])
        self.assertEqual(result, [])






class TestReduceTasks(unittest.TestCase):

    def test_sum_numbers_1_to_50_function_exists(self):
        result = Weekend2.sum_numbers_1_to_50()
        self.assertIsNotNone(result)

    def test_sum_numbers_1_to_50_returns_correct_output(self):
        result = Weekend2.sum_numbers_1_to_50()
        self.assertEqual(result, sum(range(1, 51)))

    def test_find_max_function_exists(self):
        result = Weekend2.find_max([1, 2])
        self.assertIsNotNone(result)

    def test_find_max_returns_correct_output(self):
        result = Weekend2.find_max([3, 5, 9, 2, 8])
        self.assertEqual(result, 9)

    def test_concatenate_strings_function_exists(self):
        result = Weekend2.concatenate_strings(['hi', 'there'])
        self.assertIsNotNone(result)

    def test_concatenate_strings_returns_correct_output(self):
        result = Weekend2.concatenate_strings(['I', 'love', 'Python'])
        self.assertEqual(result, 'I love Python')

    def test_product_of_squares_function_exists(self):
        result = Weekend2.product_of_squares([1, 2])
        self.assertIsNotNone(result)

    def test_product_of_squares_returns_correct_output(self):
        result = Weekend2.product_of_squares([1, 2, 3, 4])
        self.assertEqual(result, 1*4*9*16)




class TestFilterMapReduceTasks(unittest.TestCase):

    def test_sum_tuples_filter_greater_than_five_function_exists(self):
        result = Weekend2.sum_tuples_filter_greater_than_five([(1, 2)])
        self.assertIsNotNone(result)

    def test_sum_tuples_filter_greater_than_five_returns_correct_output(self):
        tuples_list = [(1, 2), (3, 4), (5, 6)]
        result = Weekend2.sum_tuples_filter_greater_than_five(tuples_list)
        self.assertEqual(result, [7, 11])

    def test_sum_numeric_strings_function_exists(self):
        result = Weekend2.sum_numeric_strings(['123'])
        self.assertIsNotNone(result)

    def test_sum_numeric_strings_returns_correct_output(self):
        data = ['123', '456', '789', 'abc', 'def']
        result = Weekend2.sum_numeric_strings(data)
        self.assertEqual(result, 1368)
