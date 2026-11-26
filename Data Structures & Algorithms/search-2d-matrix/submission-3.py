class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        rl, rr = 0, n-1
        cl, cr = 0, m-1

        # search for row
        row = -1
        while rl <= rr:
            rc = rl + (rr-rl)//2
            if matrix[rc][0] <= target <= matrix[rc][-1]:
                row = rc
                break
            elif target < matrix[rc][0]:
                rr = rc - 1
            else:
                rl = rc + 1
        
        if row == -1: return False
        
        while cl <= cr:
            cc = cl + (cr-cl) // 2
            if matrix[row][cc] == target:
                return True
            elif matrix[row][cc] > target:
                cr = cc - 1
            else:
                cl = cc + 1
        
        return False


