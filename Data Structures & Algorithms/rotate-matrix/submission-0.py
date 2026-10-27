class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n // 2 + 1):
            for c in range(r, n - r - 1):
                # rotate [r, c] -> [c, n-r-1]
                x, y = r, c
                tmp = matrix[r][c]
                for _ in range(4):
                    nx, ny = y, n - x - 1
                    tmp, matrix[nx][ny] = matrix[nx][ny], tmp
                    x, y = nx, ny
