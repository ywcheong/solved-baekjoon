"""Disclaimer: This code is partially generated with LLM, but not `solve` function's implementation"""

import sys
from typing import List

# 1. LeetCode Style Class
class Solution:
    def solve(self, N: int, M: int, grid: List[str]) -> str:
        """
        주어진 격자에서 정사각형의 끊어진 변이 어느 방향인지 찾습니다.
        
        :param N: 격자의 세로 길이 (Height)
        :param M: 격자의 가로 길이 (Width)
        :param grid: 길이 M인 문자열이 N개 담긴 리스트 (예: ['...', '##.', ...])
        :return: 끊어진 방향 ("UP", "DOWN", "LEFT", "RIGHT")
        """
        # IMPLEMENT HERE: 여기에 핵심 로직을 작성하세요.
        # 백준의 STDIN/STDOUT 처리는 아래 main 블록에서 자동으로 처리됩니다.
        
        # Using two-pass algorithm
        INF = float("inf")
        imin, imax = INF, -INF
        jmin, jmax = INF, -INF

        def update_with_wall_position(i, j):
            nonlocal imin, imax, jmin, jmax
            imin = min(imin, i)
            imax = max(imax, i)
            jmin = min(jmin, j)
            jmax = max(jmax, j)

        # Pass #1: find (imin, jmin) ~ (imax, jmax)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '#':
                    update_with_wall_position(i, j)
        
        # Now, we know (imin, jmin) ~ (imax, jmax)
        # Pass #2: find empty side

        # Checking `UP` & `DOWN`
        for j in range(jmin, jmax):
            if grid[imin][j] == ".":
                return "UP"
            if grid[imax][j] == ".":
                return "DOWN"

        # Checking `LEFT` & `RIGHT`
        for i in range(imin, imax):
            if grid[i][jmin] == ".":
                return "LEFT"
            if grid[i][jmax] == ".":
                return "RIGHT"

        # Cannot happen
        assert False, "This cannot be happen"
        


# 2. Baekjoon Adapter (Infrastructure Code)
if __name__ == "__main__":
    # 빠른 입출력 설정
    input = sys.stdin.readline
    
    # 입력 파싱
    # 첫째 줄에서 N, M을 읽어옵니다.
    line_one = input().split()
    if not line_one:
        sys.exit(0)
        
    N, M = map(int, line_one)
    
    # N개의 줄을 읽어 격자 리스트를 생성합니다.
    # 개행 문자를 제거(.strip())하여 순수 데이터만 전달합니다.
    grid = [input().strip() for _ in range(N)]
    
    # 솔루션 실행
    sol = Solution()
    result = sol.solve(N, M, grid)
    
    # 출력 처리
    print(result)
