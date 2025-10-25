public class MagicSquare {

    public static boolean isMagicSquare(int[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            return false;
        }


        int size = matrix.length;

        for (int[] row : matrix) {
            if (row.length != size) {
                return false;
            }
        }

        int expectedSum = 0;
        for (int num : matrix[0]) {
            expectedSum += num;
        }

        for (int[] row : matrix) {
            int rowSum = 0;
            for (int num : row) {
                rowSum += num;
            }
            if (rowSum != expectedSum) {
                return false;
            }
        }

        for (int col = 0; col < size; col++) {
            int colSum = 0;
            for (int row = 0; row < size; row++) {
                colSum += matrix[row][col];
            }
            if (colSum != expectedSum) {
                return false;
            }
        }

        return true;
    }















    public static void main(String[] args) {
        int[][] test1 = {
            {2, 3, 5},
            {4, 5, 1},
            {4, 2, 4}
        };
        System.out.println(isMagicSquare(test1));

        int[][] test2 = {
            {5, 2, 5},
            {6, 5, 4},
            {1, 8, 3}
        };
        System.out.println(isMagicSquare(test2));

        int[][] test3 = {
            {1, 3, 1},
            {3, 1, 1},
            {1, 1, 3}
        };
        System.out.println(isMagicSquare(test3));

        int[][] test4 = {
            {2, 1},
            {1, 2}
        };
        System.out.println(isMagicSquare(test4));
    }
}
