# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))

# | 2w
# | 3(w-100) + 200
# | 5(w-10000) + 29900
# | 7(w-1_000_000) + 4979900

def energy_to_price(energy):
    if energy < 100:
        return 2 * energy
    elif energy < 10000:
        return 3 * (energy - 100) + 200
    elif energy < 1_000_100:
        return 5 * (energy - 10000) + 29900
    else:
        return 7 * (energy - 1_000_000) + 4_979_900
    
def price_to_energy(price):
    if price < 200:
        return price // 2
    elif price < 29900:
        return (price - 200) // 3 + 100
    elif price < 4_979_900:
        return (price - 29900) // 5 + 10000
    else:
        return (price - 4_979_900) // 7 + 1_000_000


def solve(priceof_energy_sum, price_diff):
    """write your logic here"""
    energy_sum = price_to_energy(priceof_energy_sum)
    
    def cond(e):
        return energy_to_price(energy_sum - e) - energy_to_price(e) <= price_diff
    
    lo, hi = 0, energy_sum // 2
    
    if cond(lo):
        return energy_to_price(lo)
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if cond(mid):   # X O O
            hi = mid
        else:           # X X O
            lo = mid

    return energy_to_price(hi)

def test():
    """write your test here"""
    assert solve(1100, 300) == 350, "Test 1"
    assert solve(35515, 27615) == 2900, "Test 2"


def main():
    """write your i/o here"""
    while True:
        priceof_energy_sum, price_diff = input_list(int)
        if priceof_energy_sum == 0 and price_diff == 0:
            return
        print(solve(priceof_energy_sum, price_diff))


test()
main()
