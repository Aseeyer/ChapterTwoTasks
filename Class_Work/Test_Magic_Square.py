import unittest
from Magic_Square import is_magic_square

class TestMagicSquare(unittest.TestCase):
    def test_that_function_is_an_empty_matrix(self):
        self.assertFalse(is_magic_square([]))

    def test_that_the_function_is_an_irregular_matrix(self):
        self.assertFalse(is_magic_square([[1, 2], [3, 4, 5]]))

    def test_that_the_matrix_is_not_a_square_matrix(self):
        self.assertFalse(is_magic_square([[1, 2, 3], [4, 5, 6]]))

    def test_that_the_rows_and_columns_gives_a_valid_magic_square(self):
        matrix = [
            [2, 3, 5],
            [4, 5, 1],
            [4, 2, 4]
        ]

        matrix2 = [
            [2, 3],
            [3, 2]
    ]
        self.assertTrue(is_magic_square(matrix))
        self.assertTrue(is_magic_square(matrix2))


    def test_that_invalid_rows_and_columns_returns_false(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertFalse(is_magic_square(matrix))

if __name__ == "__main__":
    unittest.main()
