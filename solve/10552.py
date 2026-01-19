import sys

# 1. LeetCode Style Class
class Solution:
    def solve(self, N: int, M: int, P: int, channels: list[list[int]]) -> int:
        """
        :param N: 시청자의 수
        :param M: 채널의 수
        :param P: 현재 TV 채널
        :param channels: 각 시청자가 [좋아하는 채널, 싫어하는 채널] 정보가 담긴 리스트
        :rtype: 채널이 바뀌는 횟수 (무한히 바뀌면 -1)
        """
        # IMPLEMENT HERE: 여기에 핵심 로직을 작성하세요.
        # 백준의 STDIN/STDOUT 처리는 아래 main 블록에서 자동으로 처리됩니다.
        edge = [None] * (M + 1)
        for love_channel, hate_channel in channels:
            if edge[hate_channel] is None: # 더 어린 사람이 정했으면 따르시게
                edge[hate_channel] = love_channel

        visited = [False] * (M + 1)
        this_channel, change_count = P, 0
        while True:
            if visited[this_channel]:
                return -1

            next_channel = edge[this_channel]

            if next_channel is None:
                return change_count

            visited[this_channel] = True
            change_count += 1
            this_channel = next_channel

# 2. Baekjoon Adapter (Infrastructure Code)
if __name__ == "__main__":
    # 빠른 입출력 설정
    input = sys.stdin.read

    # 전체 입력을 한 번에 읽어와 토큰화
    data = input().split()
    if not data:
        sys.exit(0)

    N = int(data[0])  # 시청자 수
    M = int(data[1])  # 채널 수
    P = int(data[2])  # 시작 채널

    # 시청자 선호도 정보 파싱 (좋아하는 채널, 싫어하는 채널)
    # 인덱스 3부터 2개씩 묶어서 처리
    channels = []
    for i in range(N):
        fav = int(data[3 + i * 2])
        hate = int(data[4 + i * 2])
        channels.append([fav, hate])

    # 솔루션 실행
    sol = Solution()
    result = sol.solve(N, M, P, channels)

    # 출력 처리
    if result is not None:
        print(result)