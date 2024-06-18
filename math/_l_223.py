class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        x = self.get_width(ax1, ax2, bx1, bx2)
        y = self.get_width(ay1, ay2, by1, by2)
        print(f'x: {x}, y: {y}')
        both_covered = x * y

        return abs(ax1 - ax2) * abs(ay1 - ay2) + abs(bx1 - bx2) * abs(by1 - by2) - both_covered

    def get_width(self, a1, a2, b1, b2: int):

        if a2 <= b1 or b2 <= a1:
            return 0
        
        if a1 <= b1 and b2 <= a2:
            return abs(b2 - b1)
        
        if b1 <= a1 and a2 <= b2:
            return abs(b2 - a1)

        if a2 >= b2:
            return abs(b2 - a1)
        
        if b2 >= a2:
            return abs(a2 - b1)

        raise ValueError(f'unexpected case: a1: {a1}, a2: {a2}, b1: {b1}, b2: {b2}')
