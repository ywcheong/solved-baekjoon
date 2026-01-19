"""Disclaimer: This code is partially generated with LLM, but not `solve` function's implementation"""

import sys
from typing import List, Tuple

# 1. LeetCode Style Class
class Solution:
    def solve(self, length: int, width: int, height: int, cubes: List[Tuple[int, int]]) -> int:
        """
        박스를 채우는데 필요한 큐브의 최소 개수를 계산합니다.

        :param length: 박스의 가로 길이 L
        :param width: 박스의 세로 길이 W
        :param height: 박스의 높이 H
        :param cubes: 큐브 정보 리스트 [(A, B), ...].
                      A는 큐브의 크기 지수(2^A), B는 해당 큐브의 개수입니다.
        :return: 필요한 큐브의 최소 개수 (채울 수 없다면 -1 반환)
        """
        # IMPLEMENT HERE: 여기에 핵심 로직을 작성하세요.
        # (2a+1) (2b+1) (2c+1) - 8abc -> 4bc + 2c + 2b + 1 + 4ac + 2a + 4ab
        # (2a+1) (2b+1) 2c -> 4(ac + bc) + 2c
        # (2a+1) 2b 2c -> 4bc
        # 2a 2b 2c -> 0
        # 4(ab * if(c%2) + bc * if(a%2) + ac * if(b%2)) + 2(c * if(a%2&b%2) +
        cube_list = [0] * 20
        for size, count in cubes:
            cube_list[size] = count
        return self.try_solve(length, width, height, cube_list, size_index=0)

    def try_solve(self, x: int, y: int, z: int, cubes: List[int], size_index: int) -> int:
        if x == 0 and y == 0 and z == 0:
            return 0

        cube_size = 2 ** size_index

        vp = x // cube_size
        vq = y // cube_size
        vr = z // cube_size

        dp = ((vp % 2) == 1)
        dq = ((vq % 2) == 1)
        dr = ((vr % 2) == 1)

        p = (vp - dp) // 2
        q = (vq - dq) // 2
        r = (vr - dr) // 2

        need_cubes = (
                4 * (p * q * dr + p * dq * r + dp * q * r)
                + 2 * (p * dq * dr + dp * q * dr + dp * dq * r)
                + (dp * dq * dr)
        )

        # print(f"$sindex={size_index} || cube({x}, {y}, {z}) <== rem:{cubes} || cube_size {cube_size}, dp={dp} dq={dq} dr={dr}, need_cubes={need_cubes}")

        remain_cubes = cubes[:]
        this_used_cubes = self.try_fulfill(need_cubes, remain_cubes, size_index)
        # print(f"$sindex={size_index} || tuc={this_used_cubes}")

        if this_used_cubes == -1:
            # this is doomsday - cannot process further
            # now, try do DIY
            result = self.try_fulfill((x // cube_size) * (y // cube_size) * (z // cube_size), cubes, size_index)
            # print(f"$sindex={size_index} || TUC-TERM >> {result}")
            return result

        next_used_cubes = self.try_solve(x - dp * cube_size, y - dq * cube_size, z - dr * cube_size, remain_cubes,
                                         size_index + 1)

        if next_used_cubes == -1:
            # print(f"$sindex={size_index} || NUC-TERM={-1}")
            return -1

        # print(f"$sindex={size_index} || tuc={this_used_cubes} + nuc={next_used_cubes} = {this_used_cubes + next_used_cubes}")
        return this_used_cubes + next_used_cubes

    def try_fulfill(self, required_cubes: int, given_cubes: List[int], size_index: int) -> int:
        total_used_cubes = 0

        for this_size_index in range(size_index, -1, -1):
            this_usable_count = min(required_cubes, given_cubes[this_size_index])

            required_cubes -= this_usable_count
            given_cubes[this_size_index] -= this_usable_count
            total_used_cubes += this_usable_count

            if required_cubes == 0:
                return total_used_cubes

            required_cubes *= 8

        return -1


# 2. Baekjoon Adapter (Infrastructure Code)
if __name__ == "__main__":
    # 빠른 입출력 설정
    input = sys.stdin.readline

    # 전체 입력을 한 번에 읽어와서 처리 (효율성)
    data = sys.stdin.read().split()
    if not data:
        sys.exit(0)

    iterator = iter(data)

    try:
        # 첫째 줄: L, W, H
        l = int(next(iterator))
        w = int(next(iterator))
        h = int(next(iterator))

        # 둘째 줄: 큐브 종류의 개수 N
        n = int(next(iterator))

        # 셋째 줄부터: 큐브의 종류 A와 개수 B
        cubes = []
        for _ in range(n):
            a = int(next(iterator))
            b = int(next(iterator))
            cubes.append((a, b))

        # 솔루션 실행
        sol = Solution()
        result = sol.solve(l, w, h, cubes)

        # 결과 출력
        print(result)

    except StopIteration:
        pass
