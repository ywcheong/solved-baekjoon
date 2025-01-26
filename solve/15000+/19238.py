# My Solution : https://github.com/ywcheong/solved-baekjoon

import sys
from collections import deque

START, DESTINATION = 0, 1


class Pos:
    @staticmethod
    def configure(board):
        Pos.board = board
        Pos.size = len(board)

    def __init__(self, x, y):
        self.x, self.y = x, y

    def get_nexts(self):
        result = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = self.x + dx
            ny = self.y + dy
            if 0 <= nx < Pos.size and 0 <= ny < Pos.size and Pos.board[nx][ny] == 0:
                result.append(Pos(nx, ny))
        return result
    
    def __repr__(self):
        return f"P({self.x},{self.y})"
    
    def __hash__(self):
        return Pos.size * self.x + self.y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y


def build_maps(passengers):
    start_map = dict()
    end_map = dict()

    for passenger_id, (start_pos, end_pos) in enumerate(passengers):
        start_map[start_pos] = passenger_id
        end_map[end_pos] = end_map.get(end_pos, []) + [passenger_id]
    
    return start_map, end_map

def move_to_closest_passenger(taxi_pos, to_deliever, start_map):
    passenger_id = start_map.get(taxi_pos, None)
    if passenger_id in to_deliever:
        return passenger_id, 0

    to_visit, visited = deque([taxi_pos]), {taxi_pos: 0}
    result = []

    while to_visit:
        vpos = to_visit.popleft()

        if result and visited[result[0]] == visited[vpos]:
            break

        for wpos in vpos.get_nexts():
            if wpos not in visited:
                visited[wpos] = visited[vpos] + 1
                to_visit.append(wpos)

                # 해당 좌표에 아직 운송하지 않은 승객이 있는지 검사
                passenger_id = start_map.get(wpos, None)
                if passenger_id in to_deliever:
                    result.append(wpos)

    # 가장 행 번호/열 번호가 작은 승객을 추출 후 승객번호와 거리를 반환
    if len(result) == 0:
        return None, None
    
    result.sort()
    result_pos = result[0]
    return start_map[result_pos], visited[result_pos]

def deliever_passenger_to_destination(start_pos, end_pos):
    to_visit, visited = deque([start_pos]), {start_pos: 0}
    while to_visit:
        vpos = to_visit.popleft()
        for wpos in vpos.get_nexts():
            if wpos not in visited:
                visited[wpos] = visited[vpos] + 1
                to_visit.append(wpos)

                if wpos == end_pos:
                    return visited[wpos]

    return None


def solve(board, passengers, init_pos, init_fuel):
    """write your solution here"""
    start_map, end_map = build_maps(passengers)
    
    taxi_pos, taxi_fuel = init_pos, init_fuel
    to_deliever = set(passenger_id for passenger_id in range(len(passengers)))
    while len(to_deliever) > 0:
        # 다음 택시 승객에게 접근
        next_passenger_id, consumed_fuel = move_to_closest_passenger(taxi_pos, to_deliever, start_map)
        if consumed_fuel is None:
            return -1
        # print(f"택시의 좌표 {taxi_pos}에서, 기다리고 계신 승객은 {to_deliever}입니다. 다음 승객은 {next_passenger_id}입니다. 연료 {taxi_fuel} 중 {consumed_fuel}을 사용합니다.")
        taxi_fuel -= consumed_fuel
        if taxi_fuel < 0:
            return -1
        
        # 다음 택시 승객을 운송
        consumed_fuel = deliever_passenger_to_destination(*passengers[next_passenger_id])
        if consumed_fuel is None:
            return -1
        # print(f"승객 {next_passenger_id}을 모십니다. {passengers[next_passenger_id][START]}에서 {passengers[next_passenger_id][DESTINATION]}으로 모십니다. 연료 {taxi_fuel} 중 {consumed_fuel}을 사용합니다.")
        taxi_fuel -= consumed_fuel
        if taxi_fuel < 0:
            return -1
        
        taxi_fuel += 2 * consumed_fuel
        taxi_pos = passengers[next_passenger_id][1]
        # print(f"연료가 {taxi_fuel}까지 충전되었습니다. 현재 택시는 {taxi_pos}에 있습니다...")
        to_deliever.remove(next_passenger_id)
        
    return taxi_fuel


def test():
    def check(left, right):
        if left == right:
            print(f"Test pass")
        else:
            print(f"Test fail: {left} != {right}")

    """write your testing here"""
    check(solve(1), 1)
    check(solve(2), 2)
    check(solve(3), 3)

def main():
    def input_one(given_type):
        return given_type(sys.stdin.readline().strip())

    def input_list(given_type):
        return list(map(given_type, input_one(str).split()))

    """write your i/o here"""
    size, passenger_num, init_fuel = input_list(int)
    board = [None for _ in range(size)]
    for i in range(size):
        board[i] = input_list(int)
    
    ix, iy = input_list(int)
    init_pos = Pos(ix-1, iy-1)

    passengers = [None for _ in range(passenger_num)]
    for i in range(passenger_num):
        sx, sy, dx, dy = input_list(int)
        passengers[i] = [Pos(sx-1, sy-1), Pos(dx-1, dy-1)]
    
    Pos.configure(board)
    print(solve(board, passengers, init_pos, init_fuel))


# test()
main()
