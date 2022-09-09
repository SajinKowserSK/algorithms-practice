class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        self.transpose(matrix)
        for row in range(0, len(matrix)):
            matrix[row] = matrix[row][::-1]
            
        
    def transpose(self, matrix):
        for row in range(0, len(matrix)):
            for col in range(row, len(matrix[0])):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row] 
                matrix[col][row] = tmp 
                
                
        