# Implementation
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(p1, p2):
        # p1 < p2
        if p1.x != p2.x:
            return p1.x < p2.x
        return p1.y < p2.y
    
    def __str__(self):
        return f"{self.x} {self.y}"

# Testing
def test():
    print("WARNING: TEST MODE")

    p1 = Point(3, 4)
    p2 = Point(1, 1)
    p3 = Point(1, -1)
    p4 = Point(2, 2)
    p5 = Point(3, 3)

    assert sorted([p1, p2, p3, p4, p5]) == [p3, p2, p4, p5, p1]

    print("TEST DONE")

# Submit
def submit():
    import sys
    n = int(input())
    points = [None] * n

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        points[i] = Point(x, y)

    for point in sorted(points):
        print(point)

# Case-switch
if __name__ == '__main__':
    submit()