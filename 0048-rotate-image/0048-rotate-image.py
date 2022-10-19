class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        first need to transpose the matrix 
        then reverse each row 

        """

        self.transpose(matrix)
        for x in range(len(matrix)):
            matrix[x] = matrix[x][::-1]

    def transpose(self, matrix):
        for row in range(0, len(matrix)):
            for col in range(row, len(matrix[0])):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp