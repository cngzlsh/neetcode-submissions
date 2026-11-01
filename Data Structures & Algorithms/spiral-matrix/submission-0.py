class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m , n = len(matrix), len(matrix[0])
        while matrix:
            # first row
            res += matrix.pop(0)

            # down
            if matrix and matrix[0]:
                for row in range(len(matrix)):
                    res.append(matrix[row].pop(-1))
            
            # left
            if matrix:
                res += matrix.pop(-1)[::-1]
            
            # up
            if matrix and matrix[0]:
                for row in range(len(matrix)-1, -1, -1):
                    res.append(matrix[row].pop(0))

        return res