import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestMagicSquare {

    @Test
    public void testThatTheFunctionIsAnEmptyMatrix() {
        int[][] matrix = {};
        assertFalse(MagicSquare.isMagicSquare(matrix));
    }

    @Test
    public void testThatTheFunctionIsAnIrregularMatrix() {
        int[][] matrix = {
            {1, 2},
            {3, 4, 5}
        };
        assertFalse(MagicSquare.isMagicSquare(matrix));
    }

    @Test
    public void testThatTheMatrixIsNotASquareMatrix() {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };
        assertFalse(MagicSquare.isMagicSquare(matrix));
    }

    @Test
    public void testThatTheRowAndColumnsGivesAValidMagicSquare() {
        int[][] matrix1 = {
            {2, 3, 5},
            {4, 5, 1},
            {4, 2, 4}
        };

        int[][] matrix2 = {
            {2, 3},
            {3, 2}
        };

        assertTrue(MagicSquare.isMagicSquare(matrix1));
        assertTrue(MagicSquare.isMagicSquare(matrix2));
    }

    @Test
    public void testThatInvalidRowsAndColumnsReturnsFalse() {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        assertFalse(MagicSquare.isMagicSquare(matrix));
    }
}
