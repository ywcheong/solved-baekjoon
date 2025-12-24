# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys


def input_one(given_type):
    return given_type(sys.stdin.readline().strip())


def input_list(given_type):
    return list(map(given_type, input_one(str).split()))


ENTER_EVENT = -5
EXIT_EVENT = -7


def solve(segments, rail_length):
    """write your code here"""
    # 1단계. 다음의 위치를 이벤트 형식으로 배열에 저장한 뒤 정렬.
    #       단, 이 과정에서 선분 길이가 철도 길이보다 긴 데이터는 모두 제외.
    #   - i번째 진입 이벤트: 각 선분 시작점
    #   - i번째 진출 이벤트: (각 선분 종료점 - 철도 길이 + 1)
    events = []
    for human_id, (start, end) in enumerate(segments):
        line_length = end - start
        if line_length <= rail_length:
            events.append((end - rail_length, human_id, ENTER_EVENT))
            events.append((start + 1, human_id, EXIT_EVENT))
    events.sort(key=lambda event: event[0])

    # 2단계. 현재 이벤트를 set으로 관리. 정렬된 이벤트 배열을 앞에서부터 탐색.
    #   - 진입 이벤트 시 set 삽입.
    #   - 진출 이벤트 시 set 추출.
    #   - 각 이벤트 처리 직후 최대 길이 유지.
    last_event_pos, known_max = None, 0
    enter_set = set()
    for event_pos, human_id, event_type in events:
        if event_pos != last_event_pos:
            known_max = max(known_max, len(enter_set))
            last_event_pos = event_pos

        if event_type == ENTER_EVENT:
            enter_set.add(human_id)
        else:
            enter_set.remove(human_id)

    print(known_max)
    return


def main():
    """write your code here"""
    # size <= 100_000
    size = input_one(int)
    segments = [None] * size

    for i in range(size):
        a, b = input_list(int)
        if a > b:
            a, b = b, a
        segments[i] = (a, b)

    rail_length = input_one(int)
    solve(segments, rail_length)


main()
