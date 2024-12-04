# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
import heapq

MOD = 2_000_003


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def is_divisible(num, prime_list):
    upper_limit = int(num ** 0.5) + 1
    for prime in prime_list:
        if prime > upper_limit:
            return False
        if num % prime == 0:
            return True
    return False


def get_next_prime(prime_list):
    num = prime_list[-1] + 1
    while is_divisible(num, prime_list):
        num += 1
    return num


class Factor:
    def __init__(self, prime):
        self.prime = prime
        self.power = 0
        self._compute_next_increment()

    def increase(self):
        power_increment = self.power + 1
        self.power += power_increment
        result = self._next_increment
        self._compute_next_increment()
        return result
    
    def _compute_next_increment(self):
        power_increment = self.power + 1
        value_increment = (self.prime ** power_increment)
        self._next_increment = value_increment

    def __lt__(s1, s2):
        return s1._next_increment < s2._next_increment
    
    def __str__(self):
        return f"F[{self.prime}^{self.power}::s::{self._next_increment}]"
        

def solve(beta):
    """write your logic here"""
    alpha = 1
    prime_list = [2]
    factor_heap = [Factor(2)]
    
    for iter_id in range(beta):
        # find this prime-factor
        this_factor = heapq.heappop(factor_heap)
        # print(f"Iter({iter_id+1}/{beta})::pick -> {this_factor}")

        # check if this prime is first-time use
        # if yes, push new prime also
        if this_factor.prime == prime_list[-1]:
            next_prime = get_next_prime(prime_list)
            # print(f"New prime: {next_prime}")
            prime_list.append(next_prime)
            heapq.heappush(factor_heap, Factor(next_prime))

        # update alpha
        # modify prime-factor and push
        alpha = (alpha * this_factor.increase()) % MOD
        heapq.heappush(factor_heap, this_factor)
        # print(f"Iter({iter_id+1}/{beta})::report -> {"".join(map(str, factor_heap))}")

    return alpha % MOD # , "".join(map(str, factor_heap))


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your test here"""
    check(is_divisible(4, [2, 3]), True)
    check(solve(0), 1)
    check(solve(1), 2)
    check(solve(7), 83160)

    prime = [2]
    for num in range(3, 30):
        if not is_divisible(num, prime):
            prime.append(num)
    check(prime, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


def main():
    """write your i/o here"""
    beta = input_one(int)
    print(solve(beta))


# test()
main()
