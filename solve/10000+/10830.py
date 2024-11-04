# My Solution : https://github.com/ywcheong/solved-baekjoon

# Header
''' import header here '''


import sys
input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

TESTCASE_ID = 1
def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1

# Implementation
''' write code here '''
class Matrix:

    CLIP_VALUE = 1000

    def __init__(self, table):
        self.table = Matrix.zeros(len(table))
        for i in range(len(table)):
            for j in range(len(self.table)):
                self.table[i][j] = table[i][j] % 1000


    def __len__(self):
        return len(self.table)
    
    def __mul__(self, other):
        A, B = self.table, other.table
        assert len(A) == len(B)
        size = len(A)

        C = Matrix.zeros(size)
        for p in range(size):
            for q in range(size):
                for i in range(size):
                    C[p][q] = (C[p][q] + A[p][i] * B[i][q]) % Matrix.CLIP_VALUE

        return Matrix(C)

    def __pow__(A, n: int):
        """
        Returns A ** n
        """
        if n == 0:
            return Matrix.identity(len(A))
        elif n == 1:
            return A
        elif n == 2:
            return A * A
        elif n % 2 == 0:
            return (A ** (n // 2)) ** 2
        else:
            return ((A ** (n // 2)) ** 2) * A
        
    def __str__(self):
        return "\n".join([" ".join(map(str, self.table[i])) for i in range(len(self))])
    
    @classmethod
    def zeros(cls, size):
        """
        Returns $$0 \in \mathbb{R}^{\text{size} \times \text{size}}$$
        """
        return [[0 for j in range(size)] for i in range(size)]
        
    @classmethod
    def identity(cls, size):
        """
        Returns $$I \in \mathbb{R}^{\text{size} \times \text{size}}$$
        """
        return [[(1 if i == j else 0) for j in range(size)] for i in range(size)]

# Testing
def test():
    print("WARNING: TEST MODE")

    ''' test here '''
    # equal(1, 1) -> OK (1 == 1)
    # equal(2, 1) -> FAIL (2 == 1)
    equal(str(Matrix([
        [1, 2],
        [3, 4]
    ]) ** 5), """69 558
337 406""")
    
    equal(str(Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]) ** 3), """468 576 684
62 305 548
656 34 412""")
    
    equal(str(Matrix([
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
    ]) ** 10), """512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512""")

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    size, power = input_list(int)
    table = [None] * size
    for i in range(size):
        table[i] = input_list(int)
    print(Matrix(table) ** power)

# Case-switch
if __name__ == '__main__':
    # test()
    submit()