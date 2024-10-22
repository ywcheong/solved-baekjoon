# Algorithm Study
Youngwoon Cheong (yw.ch@kaist.ac.kr)

# 3부 알고리즘 설계 패러다임

## 6장 무식하게 풀기
### 6.2 재귀 호출과 완전 탐색
#### 백트래킹
```py
def backtrack(state) -> None:
    if is_solution(state):
        do_something_with_solution(state)
        return
    
    for choice in get_choices(state):
        if is_valid(state, choice):
            state.add(choice)
            backtrack(state)
            state.remove(choice)
```

### 6.7 최적화 문제
* 쉬움
    * ???
* 보통
    * ???
* 어려움
    * ???

### 6.10 많이 등장하는 완전 탐색 유형
이분 탐색
```
lower_bound(L, k) = i
	<-> L[i-1] < k <= L[i]

[1, 2, ..., k-1, k+1]
                 ^ index of LB

[1, 2, ..., k-1, k, k+1]
                 ^ index of LB

"제가 계산한 인덱스 이상은 전부 >= k에요"

upper_bound(L, k) = i
	<-> L[i-1] <= k < L[i]

[1, 2, ..., k-1, k+1]
            ^ index of UB

[1, 2, ..., k-1, k, k+1]
                 ^ index of UB

"제가 계산한 인덱스 이하는 전부 <= k에요"
```

## 7장 분할 정복
* 쉬움
    * ???
* 보통
    * ???
* 어려움
    * ???

## 8장 동적 계획법
* 쉬움
    * ???
* 보통
    * ???
* 어려움
    * ???

## 9장 동적 계획법 테크닉

## 10장 탐욕법
```
Well Ordering Principle

Suppose Solution by Greedy as O*
Suppose O* is not an optimal, but O- is.

Let
    O* = {i1, i2, ..., ik-1, ik, ik+1, ..., in}
    O- = {i1, i2, ..., ik-1, i'k, i'k+1, ..., i'n}

PROVE THAT O+ = O- - {i'k} + {ik} is optimal.
```

## 11장 조합 탐색
### 11.2 조합 탐색 기법들
### 11.9 더 읽을거리

## 12장 최적화 문제 결정 문제로 바꿔 풀기

# 4부 유명한 알고리즘들

## 13장 수치 해석
### 13.1 도입
### 13.2 이분법
### 13.3 문제: 승률 올리기 (문제 ID: RATIO, 난이도: 하)
### 13.4 풀이: 승률 올리기
### 13.5 삼분 검색
### 13.6 문제: 꽃가루 화석 (문제 ID: FOSSIL, 난이도: 상)
### 13.7 풀이: 꽃가루 화석
### 13.8 다른 주제들

## 14장 정수론
### 14.1 도입
### 14.2 소수
### 14.3 문제: 비밀번호 486 (문제 ID: PASS486, 난이도: 중)
### 14.4 풀이: 비밀번호 486
### 14.5 유클리드 알고리즘
### 14.6 문제: 마법의 약 (문제 ID: POTION, 난이도: 중)
### 14.7 풀이: 마법의 약
### 14.8 모듈라 연산
### 14.9 더 읽을거리(OPTIONAL)

## 15장 계산 기하
### 15.1 도입
### 15.2 계산 기하의 도구들
### 15.3 교차와 거리, 면적
### 15.4 문제: 핀볼 시뮬레이션 (문제 ID: PINBALL, 난이도: 상)
### 15.5 풀이: 핀볼 시뮬레이션
### 15.6 다각형
### 15.7 문제: 보물섬 (문제 ID: TREASURE, 난이도: 상)
### 15.8 풀이: 보물섬
### 15.9 문제: 너드인가, 너드가 아닌가? (문제 ID: NERDS, 난이도: 중)
### 15.10 풀이: 너드인가, 너드가 아닌가?
### 15.11 계산 기하 알고리즘 디자인 패턴
### 15.12 자주 하는 실수와 유의점들
### 15.13 더 읽을거리

# 5부 기초 자료 구조

## 16장 비트마스크
### 16.1 도입
### 16.2 비트마스크를 이용한 집합의 구현
### 16.3 비트마스크의 응용 예제
### 16.4 문제: 졸업 학기 (문제 ID: GRADUATION, 난이도: 중)
### 16.5 풀이: 졸업 학기
### 16.6 더 읽을거리

## 17장 부분 합
### 17.1 도입
### 17.2 문제: 크리스마스 인형 (문제 ID: CHRISTMAS, 난이도: 중)
### 17.3 풀이: 크리스마스 인형
### 17.4 더 공부할 거리

## 18장 선형 자료 구조
### 18.1 도입
### 18.2 동적 배열
### 18.3 연결 리스트
### 18.4 동적 배열과 연결 리스트의 비교
### 18.5 문제: 조세푸스 문제 (문제 ID: JOSEPHUS, 난이도: 하)
### 18.6 풀이: 조세푸스 문제
### 18.7 더 읽을 거리

## 19장 큐와 스택, 데크
### 19.1 도입
### 19.2 큐와 스택, 데크의 구현
### 19.3 스택과 큐의 활용
### 19.4 문제: 짝이 맞지 않는 괄호 (문제 ID: BRACKETS2, 난이도: 하)
### 19.5 풀이: 짝이 맞지 않는 괄호
### 19.6 문제: 외계 신호 분석 (문제 ID: ITES, 난이도: 중)
### 19.7 풀이: 외계 신호 분석

## 20장 문자열
### 20.1 도입
### 20.2 문자열 검색
### 20.3 문제: 재하의 금고 (문제 ID: JAEHASAFE, 난이도: 중)
### 20.4 풀이: 재하의 금고
### 20.5 접미사 배열
### 20.6 문제: 말버릇 (문제 ID: HABIT, 난이도: 중)
### 20.7 풀이: 말버릇
### 20.8 더 읽을거리

# 6부 트리

## 21장 트리의 구현과 순회
### 21.1 도입
### 21.2 트리의 순회
### 21.3 문제: 트리 순회 순서 변경 (문제 ID: TRAVERSAL, 난이도: 하)
### 21.4 풀이: 트리 순회 순서 변경
### 21.5 문제: 요새 (문제 ID: FORTRESS, 난이도: 중)
### 21.6 풀이: 요새

## 22장 이진 검색 트리
### 22.1 도입
### 22.2 이진 검색 트리의 정의와 조작
### 22.3 시간 복잡도 분석과 균형 잡힌 이진 검색 트리
### 22.4 문제: 너드인가, 너드가 아닌가? 2 (문제 ID: NERD2, 난이도: 중)
### 22.5 풀이: 너드인가, 너드가 아닌가? 2
### 22.6 균형 잡힌 이진 검색 트리 직접 구현하기: 트립
### 22.7 문제: 삽입 정렬 뒤집기 (문제 ID: INSERTION, 난이도: 중)
### 22.8 풀이: 삽입 정렬 뒤집기

## 23장 우선순위 큐와 힙
### 23.1 도입
### 23.2 힙의 정의와 구현
### 23.3 문제: 변화하는 중간 값 (문제 ID: RUNNINGMEDIAN, 난이도: 하)
### 23.4 풀이: 변화하는 중간 값

## 24장 구간 트리
### 24.1 구간 트리: 구간에 대한 질문 대답하기
### 24.2 문제: 등산로 (문제 ID: MORDOR, 난이도: 중)
### 24.3 풀이: 등산로
### 24.4 문제: 족보 탐험 (문제 ID: FAMILYTREE, 난이도: 상)
### 24.5 풀이: 족보 탐험
### 24.6 펜윅 트리: 빠르고 간단한 구간 합
### 24.7 문제: 삽입 정렬 시간 재기 (문제 ID: MEASURETIME, 난이도: 중)
### 24.8 풀이: 삽입 정렬 시간 재기

## 25장 상호 배타적 집합
### 25.1 도입
### 25.2 문제: 에디터 전쟁 (문제 ID: EDITORWARS, 난이도: 중)
### 25.3 풀이: 에디터 전쟁

## 26장 트라이
### 26.1 도입
### 26.2 문제: 안녕히, 그리고 물고기는 고마웠어요! (문제 ID: SOLONG, 난이도: 중)
### 26.3 풀이: 안녕히, 그리고 물고기는 고마웠어요!
### 26.4 트라이를 이용한 다중 문자열 검색
### 26.5 문제: 보안종결자 (문제 ID: NH, 난이도: 상)
### 26.6 풀이: 보안종결자

# 7부 그래프

## 27장 그래프의 표현과 정의
### 27.1 도입
### 27.2 그래프의 사용 예
### 27.3 암시적 그래프 구조들
### 27.4 그래프의 표현 방법

## 28장 그래프의 깊이 우선 탐색
## 29장 그래프의 너비 우선 탐색
```python
# BFS, DFS (주의: 아래 코드는 Connected Graph에서만 작동)
def get_distance(start):
    to_visit, visited = \
        [(0, start)], {start: 0}

    while to_visit: # 여전히 노드가 남아 있다면...
        dist, v = heapq.heappop(to_visit)
        if dist > visited.get(v, float('inf')):
            continue
        for w, weight in edge(v):   # edge 함수로 구현하든, dict를 쓰든...
            new_dist = visited[v] + weight
            if w not in visited or new_dist < visited[w]:    # 방문한 적이 없거나 더 짧은 경로를 찾았다면
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return visited
```

## 30장 최단 경로 알고리즘
최단경로 문제는 4가지로 나눌 수 있다.
* **단일** 출발, **단일** 도착 `(p -> q)`
    * 단일-전체의 하위문제
* **단일** 출발, **전체** 도착 `(p -> B)`
    * 음수 edge 부재 = 다익스트라
    * 음수 edge 존재 = 벨만-포트
* **전체** 출발, **단일** 도착 `(A -> q)`
    * 그래프 방향을 반대로 뒤집으면 `단일출발 전체도착`과 동일한 경우이다.
* **전체** 출발, **전체** 도착 `(A -> B)`

### 30.2 다익스트라 알고리즘
* **단일** 출발, **전체** 도착.
* 음수 edge 존재 시 틀림
* 암기: Dijkstra (D-efault)
* $O(v^2 + e)$

```python
import heapq

def edge(v):
    return [('distance_1', 'node_1'), ('distance_2', 'node_2')]

def get_shortest(start):
    to_visit, visited = [(0, start)], {start: 0}

    while to_visit:
        dist, v = heapq.heappop(to_visit)
        
        # "만료된 노드 삭제" - 아래 참고
        if dist > visited.get(v, float("inf")):
            continue
        assert dist == visited.get[v]

        # 탐색 시작
        for weight, w in edge(v):
            new_dist = dist + weight
            #  (미개척 노드거나)  or  (더 나은 개척로가 있거나)
            if w not in visited or new_dist < visited[w]:
                # heappush를 함으로써 기존 (old_dist, w)는 "만료된 노드 삭제"에서 걸러짐
                # w not in visited 조건을 활용해, 더 좋은 해가 아닌 경우에는 heappush 안함
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return visited
```

### 30.9 벨만-포드 알고리즘
* **단일** 출발, **전체** 도착 (= 다익스트라)
* 음수 cycle 탐지 가능
* 암기: Bellman-Ford (B-etter)
* $O(ve) (\approx O(v^3))$

```python
def get_shortest(graph, start):
    pass
```

### 30.12 플로이드-워셜 알고리즘
* **전체** 출발, **전체** 도착
* 음수 cycle 탐지 가능
* 암기: Floyd-Warshall (F-ull)
* $O(v^3)$

```python
def get_shortest(node_count, edge):
    '''edge: edge[i][j] = (i -> j dist) or None'''
    dist = [[float("inf")] * node_count for _ in range(node_count)]
    for start in range(node_count):
        for end in range(node_count):
            if edge[start][end] is not None:
                # initialize dist with edge
                dist[start][end] = min(dist[start][end], edge[start][end])
    for mid in range(node_count):
        for start in range(node_count):
            for end in range(node_count):
                # update each dist for every possible mids
                dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
    return dist
```

## 31장 최소 스패닝 트리
### 31.1 도입
### 31.2 크루스칼의 최소 스패닝 트리 알고리즘
### 31.3 프림의 최소 스패닝 트리 알고리즘
### 31.4 문제: 근거리 네트워크 (문제 ID: LAN, 난이도: 하)
### 31.5 풀이: 근거리 네트워크
### 31.6 문제: 여행 경로 정하기 (문제 ID: TPATH, 난이도: 상)
### 31.7 풀이: 여행 경로 정하기

## 32장 네트워크 유량
### 32.1 도입
### 32.2 포드-풀커슨 알고리즘
### 32.3 네트워크 모델링
### 32.4 문제: 승부 조작 (문제 ID: MATCHFIX, 난이도: 중)
### 32.5 풀이: 승부 조작
### 32.6 문제: 국책 사업 (문제 ID: PROJECTS, 난이도: 상)
### 32.7 풀이: 국책 사업
### 32.8 이분 매칭
### 32.9 문제: 비숍 (문제 ID: BISHOPS, 난이도: 중)
### 32.10 풀이: 비숍
### 32.11 문제: 함정 설치 (문제 ID: TRAPCARD, 난이도: 상)
### 32.12 풀이: 함정 설치
### 32.13 더 공부할 거리
