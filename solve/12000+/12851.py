# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


def get_next(pos):
    return [next_pos for next_pos in [pos + 1, pos - 1, 2 * pos] if next_pos < 200_000]


def main():
    """write your code here"""
    start, target = input_list(int)

    # visited[pos] = pos까지 도착하는 tuple(최단시간, 최단시간으로 방문 가능한 횟수)
    to_visit, visited = deque(), dict()
    to_visit.append(start)
    visited[start] = (0, 1)

    while to_visit:
        vpos = to_visit.popleft()
        vtime, vcount = visited[vpos]

        # 현재 탐색중인 영역에서 아무리 빠르게 target으로 가도
        # 알려진 target의 최단시간보다 빠르게 갈 수 없는지 파악
        if visited.get(target, [float("inf")])[0] <= vtime:
            # 만약 그럴 경우, 탐색을 중단하고 결과 반환
            ttime, tcount = visited[target]
            print(f"{ttime}\n{tcount}\n")
            return

        # 인접 노드 w 방문
        for wpos in get_next(vpos):
            # Case 1. w 미방문 -> 다음 방문지로 w 지정
            if wpos not in visited:
                to_visit.append(wpos)
                visited[wpos] = (vtime + 1, vcount)
            # Case 2. w 방문 -> 다음 방문지로 w는 생략
            else:
                wtime, wcount = visited[wpos]
                if (
                    wtime > vtime + 1
                ):  # Case 2-a. 알려진 것보다 빠르게 도착 (불가능하긴 함)
                    visited[wpos] = (vtime + 1, vcount)
                    print("Wtf")
                elif wtime == vtime + 1:  # Case 2-b. 알려진 것과 똑같이 도착
                    visited[wpos] = (vtime + 1, vcount + wcount)
                else:  # Case 2-c. 알려진 것보다 느리게 도착 -> 무시
                    pass

    # 주어진 조건에 의해, 모든 노드는 최소 1회 방문
    # 따라서 반드시 종료함
    raise AssertionError("Unreachable Point")


main()
