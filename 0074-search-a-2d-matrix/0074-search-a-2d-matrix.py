class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0]) if row > 0 else 0
        low = 0
        high = row * col -1
        while(low <= high):
            mid = low + (high - low) / 2
            r = mid / col
            c = mid % col
            if (matrix[r][c] == target):
                return True
            else:
                if matrix[r][c] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
