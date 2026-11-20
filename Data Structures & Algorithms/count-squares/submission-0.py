from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.xs = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for y2, c in list(self.xs[x].items()):
            if y2 == y:
                continue
            side = y2 - y
            for x1 in (x + side, x - side):
                col = self.xs.get(x1)
                if col:
                    res += c * col.get(y, 0) * col.get(y2, 0)
        return res