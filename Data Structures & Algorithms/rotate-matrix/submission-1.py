class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # only need to perform operations in the top quarter
        for r in range(n // 2):
            for c in range(r, n - r -1):
                cur = matrix[r][c]
                
                for _ in range(4):
                    # (i, j) -> (j, n-i-1)
                    tr, tc = c, n - r - 1
                    tmp = matrix[tr][tc]
                    matrix[tr][tc] = cur
                    cur = tmp
                    r, c = tr, tc
