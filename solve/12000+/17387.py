# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from fractions import Fraction


def matrix_times_vector(matrix, vector):
    a, b = matrix[0]
    c, d = matrix[1]
    p, q = vector
    return [a * p + b * q, c * p + d * q]


def matrix_time_matrix(m1, m2):
    a, b = m1[0]
    c, d = m1[1]
    p, q = m2[0]
    r, s = m2[1]

    return [[a * p + b * r, a * q + b * s], [c * p + d * r, c * q + d * s]]


def det(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c


def inverse_matrix(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    n = det(matrix)

    return [[d / n, -b / n], [-c / n, a / n]]


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def solve(L1, L2):
    """write your code here"""
    x1, y1, x2, y2 = map(Fraction, L1)
    x3, y3, x4, y4 = map(Fraction, L2)

    a, b = x2 - x1, x3 - x4
    c, d = y2 - y1, y3 - y4
    v, w = x3 - x1, y3 - y1

    # Amat     Pvec    Vvec
    # | a b | | p | = | v |
    # | c d | | q |   | w |

    Amat = [[a, b], [c, d]]
    Vvec = [v, w]
    #print(f"Amat={Amat} * pvec = Vvec{Vvec}")

    if det(Amat) != 0:
        p, q = matrix_times_vector(inverse_matrix(Amat), Vvec)
        #print(f"Detzero p={p} q={q}")
        return 0 <= p <= 1 and 0 <= q <= 1

    if a == b == 0:
        a, b, v, c, d, w = c, d, w, a, b, v

    if c != 0:
        a, b, v, w = a * c, b * c, v * c, -v * c + a * w
        Amat = [[a, b], [c, d]]
        Vvec = [v, w]
        #print(f"re: Amat={Amat} * pvec = Vvec{Vvec}")

    if w != 0:
        #print(f"Imps w={w}")
        return False
    
    #print(f"Cvval (a={a})p + (b={b})q - (v={v}) ><= 0")

    checks = [a * p + b * q - v for p, q in [(0, 0), (0, 1), (1, 0), (1, 1)]]
    checks.sort()

    #print(f"Dcheck checks={checks}")
    return checks[-1] * checks[0] <= 0


def test():
    print(solve([1, 1, 5, 5], [1, 5, 5, 1]) == bool(1))  # 1
    print(solve([1, 1, 5, 5], [6, 10, 10, 6]) == bool(0))  # 2
    print(solve([1, 1, 5, 5], [5, 5, 1, 1]) == bool(1))  # 3
    print(solve([1, 1, 5, 5], [3, 3, 5, 5]) == bool(1))  # 4
    print(solve([1, 1, 5, 5], [3, 3, 1, 3]) == bool(1))  # 5
    print(solve([1, 1, 5, 5], [5, 5, 9, 9]) == bool(1))  # 6
    print(solve([1, 1, 5, 5], [6, 6, 9, 9]) == bool(0))  # 7
    print(solve([1, 1, 5, 5], [5, 5, 1, 5]) == bool(1))  # 8
    print(solve([1, 1, 5, 5], [6, 6, 1, 5]) == bool(0))  # 9
    print(solve([0, 0, 0, 1], [0, 2, 0, 3]) == bool(0))  # 10
    print(solve([0, 0, 0, 1], [0, 1, 0, 3]) == bool(1))  # 10


def main():
    L1, L2 = input_list(int), input_list(int)
    print(int(solve(L1, L2)))


main()
