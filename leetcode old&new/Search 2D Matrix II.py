class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1 # starting at end of the row since we know that's the highest value

        # while we are within bounds
        while row < len(matrix) and col >= 0:
            curr = matrix[row][col]

            if curr == target:
                return True

            # if curr elem is greater than target and we are at the end of a row's value (greatest val in row)
            # we can move left to get a smaller curr val
            elif curr > target:
                col -= 1

            # curr is now too small, we've been going RIGHT to LEFT so going back right to look for a greater
            # elem would be useless

            # instead we can take advantage of how the cols are also increasing so shift down one
            else:  # curr > target
                row += 1

        return False

