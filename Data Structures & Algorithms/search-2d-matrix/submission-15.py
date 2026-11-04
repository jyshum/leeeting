class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = (rows * cols) - 1

        while right >= left:
            middle = (left+right) // 2
            row = middle // cols
            col = middle % cols
            value = matrix[row][col]

            if target == value:
                return True
            elif target < value:
                right = middle - 1
            elif target > value:
                left = middle + 1
        
        return False

