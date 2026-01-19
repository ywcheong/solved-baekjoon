import sys


# 1. LeetCode Style Class
class Solution:
    def solve(self, N: int, given_days: list[int]) -> bool:
        """
        :param N: 일의 개수 (1 <= N <= 1,000)
        :param given_days: 각 일의 작업 소요 시간 리스트 (1 <= A_i <= 10^5)
        :return: 금요일에 마칠 수 있으면 True, 없으면 False
        """
        # IMPLEMENT HERE: 여기에 핵심 로직을 작성하세요.
        possible_days = [False] * 7
        for day in given_days:
            new_day = day % 7
            new_possible_days = possible_days[:] # GC 최적화된 코드는 아님
            for each_day in range(7):
                if possible_days[each_day]:
                    new_possible_days[(each_day + new_day) % 7] = True
            new_possible_days[new_day] = True
            possible_days = new_possible_days

        return possible_days[4]

# 2. Baekjoon Adapter (Infrastructure Code)
if __name__ == "__main__":
    # 빠른 입출력 설정
    input = sys.stdin.read

    # 데이터 전체 읽기 및 파싱
    data = input().split()
    if not data:
        sys.exit(0)

    N = int(data[0])
    A = list(map(int, data[1:]))

    # 솔루션 실행
    sol = Solution()
    result = sol.solve(N, A)

    # 출력 처리 (YES/NO 형식)
    if result:
        print("YES")
    else:
        print("NO")