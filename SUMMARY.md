# Python Algorithm Study Summary Note
Youngwoon Cheong (tencise@gmail.com)

## Table of Contents
- [Python Algorithm Study Summary Note](#python-algorithm-study-summary-note)
  - [Table of Contents](#table-of-contents)
  - [Time Complexity Analysis](#time-complexity-analysis)
    - [Asymptotic Notation of Time Complexity](#asymptotic-notation-of-time-complexity)
    - [Master Theorem](#master-theorem)
  - [Searching](#searching)
    - [Backtracking](#backtracking)
    - [Parametric Search](#parametric-search)
    - [Binary Search](#binary-search)
  - [Optimization](#optimization)
    - [Dynamic Programming (TODO)](#dynamic-programming-todo)
    - [Divide and Conquer (TODO)](#divide-and-conquer-todo)
    - [Greedy (TODO)](#greedy-todo)
  - [Data Structure (TODO)](#data-structure-todo)
    - [Stack](#stack)
    - [Queue](#queue)
    - [Heap](#heap)
    - [Linked List (TODO)](#linked-list-todo)
    - [Balanced Tree (TODO)](#balanced-tree-todo)
    - [Segment Tree (TODO)](#segment-tree-todo)
    - [Bitmask (TODO)](#bitmask-todo)
    - [Disjoint Set](#disjoint-set)
  - [String (TODO)](#string-todo)
  - [Graph](#graph)
    - [Search - BFS \& DFS](#search---bfs--dfs)
    - [Shortest Path](#shortest-path)
      - [Dijkstra](#dijkstra)
      - [Bellman-Ford (TODO)](#bellman-ford-todo)
      - [Floyd-Warshall (TODO)](#floyd-warshall-todo)
    - [Min Spanning Tree](#min-spanning-tree)
      - [Prim (TODO)](#prim-todo)
      - [Kruskal](#kruskal)
    - [Network Flow (TODO)](#network-flow-todo)
      - [Ford-Fulkerson (TODO)](#ford-fulkerson-todo)
      - [Bipartite Matching (TODO)](#bipartite-matching-todo)
  - [Geometry (TODO)](#geometry-todo)
  - [Numeric Analysis (TODO)](#numeric-analysis-todo)


## Time Complexity Analysis

### Asymptotic Notation of Time Complexity
* Upper-strict-bound $o(f(n))$
* **Upper-equal-bound** $O(f(n))$
* Equal-bound $\Theta(f(n))$
* Lower-equal-bound $\Omega(f(n))$
* Lower-strict-bound $\omega(f(n))$

### Master Theorem
Let $T(n)$ the time complexity function s.t.

$$
    T(n) = a T(\frac{n}{b}) + f(n)
$$

Then, naïvely,

$$
T(n) \in
\begin{cases}
\Theta(n^{\log_b a}) & : f(n) \in o(n^{\log_b a}) \\
\Theta(n^{\log_b a} \log n) & : f(n) \in \Theta(n^{\log_b a}) \\
\Theta(f(n)) & : f(n) \in \omega(n^{\log_b a}) \\
\end{cases}
$$

## Searching
### Backtracking
* Small search space
* Require traversing every cases

```python
# Backtracking - Python
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

### Parametric Search

* Search space is sorted or total-ordered
* Can implement `cond` function


```python
# Parametric Search - Python
def parametric_search(lo, hi, cond):
    assert not cond(lo) and cond(hi)    # X ... O
    while lo + 1 < hi:                  # X  ?  O
        mid = (lo + hi) // 2
        if cond(mid):                   # X  O  O
            hi = mid
        else:                           # X  X  O
            lo = mid
    return lo, hi                       # X O

```
* Note that you can use lo, hi as **out-of-bound**.
  * For example, `L = [1, 2, 3]` and `cond = (x) => (4 <= x)`
  * You can use `lo, hi = -1, len(L)` then you get `lo, hi = 2, 3`

### Binary Search

* This is a special case of the [Parametric Search](#parametric-search).
  * Given nondecreasing list `L`, you want to find `x`.
  * Let `lo, hi = -1, len(L)`, `cond = (mid) => (x <= L[mid])`
  * For the parametric search result, check `hi != len(L) and L[hi] == x`

## Optimization
### Dynamic Programming (TODO)

### Divide and Conquer (TODO)

### Greedy (TODO)
* Well Ordering Principle
  * Suppose Solution by Greedy as $O^*$
  * Suppose $O^*$ is not an optimal, but $O^-$ is.
  * Let
    * $O^* = \{i_1, i_2, ..., i_{k-1}, i_k, i_{k+1}, ..., i_n\}$
    * $O^- = \{i_1, i_2, ..., i_{k-1}, i^{-}_{k}, i^{-}_{k+1}, ..., i^{-}_{n}\}$
  * Prove $O^+ = O^- - \{i^{-}_{k}\} + \{i_k\}$ is optimal, which is a contradiction. $\blacksquare$

## Data Structure (TODO)

### Stack
* First In Last Out (FILO)
* Time Complexity
  * Insert, Pop, Top $O(1)$
* Use Cases
  * Shunting Yard
    * Given infix arithmetic, convert into postfix.
```python
stack = list()
```

### Queue
* First In First Out (FIFO)
* Time Complexity
  * Same with stack
* Use Cases
```python
from collections import deque
queue = deque()
```

### Heap
* Smallest First Out
* Time Complexity
  * Top $O(1)$
  * Insert, Pop $O(\log n)$
* Use Cases
  * Dijkstra
```python
import heapq
my_heap = []
heapq.heappush(my_heap, (weight, extra))
assert my_heap[0] == (weight, extra)
assert heapq.heappop(my_heap) == (weight, extra)
```

### Linked List (TODO)

### Balanced Tree (TODO)

### Segment Tree (TODO)

### Bitmask (TODO)

### Disjoint Set
* Split given set into partitions
* Time Complexity
  * Check partition of element $\approx O(1)$
  * Union(merge) two partition of given two element $O(1)$
* Usase
  * Kruskal MST

```python
# Disjoint Set - Python
class DisjointSet:
    '''Partition N elements'''
    def __init__(self, n):
        self.parent = [x for x in range(n)]
    def get_parent(self, x):
        if x != self.parent[x]:
            self.parent[x] = get_root(self.parent[x])
        return self.parent[x]
    def unify_parent(x, y):
        x, y = self.get_parent(x), self.get_parent(y)
        if x != y:
            self.parent[y] = x
```

## String (TODO)

## Graph
Graph $G = (V, E)$ while $E \subseteq V \times V$.

In here we represent graph in the form of `graph = dict[v, List[w]]`.

### Search - BFS & DFS
```python
# BFS & DFS - Python
from collections import deque

def xfs_traverse(
    edge: dict[node, List[node]],
    start: node
):
    to_visit, depth = deque([start]), {start: 0}

    while to_visit: # still, there is a node to visit...
        v = to_visit.pop()  # .pop() for DFS, .popleft() for BFS
        for w in graph[v]:
            if w not in depth:
                to_visit.append(w)
                depth[w] = depth[v] + 1
    
    return depth
```
### Shortest Path
There are four types of shortest path problems.
1. **Single** start, **Single** end
    * Subproblem of case #2
2. **Single** start, **Every** end
    * $\forall e \in G : w(e) \ge 0 :$ `Dijkstra`
    * $\exists e \in G : w(e) < 0 :$ `Bellman-Ford`
3. **Every** start, **Single** end
    * Reduction of case #2
4. **Every** start, **Every** end
    * `Floyd-Warshall`

#### Dijkstra
* **Single** start, **Every** end
* Does **NOT** work when negative weight edge exists
  * Use Bellman-ford instead in the case
* Time Complexity $O(v \log e)$
```python
# Dijkstra - Python
import heapq

def shortest_dijkstra(
    graph: dict[node, List[tuple[float, node]]],
    start: node
):
    to_visit, visited = [(0, start)], {start: 0}

    while to_visit:
        dist, v = heapq.heappop(to_visit)

        # Outdated v - remove
        if visited[v] < dist:
            continue

        for weight, w in graph[v]:
            new_dist = dist + weight
            # (Not visited) or (Found better)
            if (w not in visited) or (new_dist < dist[w]):
                heapq.heappush(to_visit, (new_dist, w))
                visited[w] = new_dist

    return visited
```

#### Bellman-Ford (TODO)

#### Floyd-Warshall (TODO)

### Min Spanning Tree
$G^*$ is MST when given a weight function of edges $w: E \rightarrow \mathbb{R}^{+}$:

$$
G = (V, E^*) \text{ s.t. } E^* =
\argmin_{\substack{E^* \subseteq E \\ |E^*|=|V|-1}}{
    \sum_{e \in E^{*}}{w(e)}
}
$$

#### Prim (TODO)

#### Kruskal
* Sort edges in the ascending order of weight
* Take edges using greedy method, but not cycle-forming one
* Time complexity: $O(e \log e)$
  * Time complexity of Disjoint Set: $\approx O(1)$
```python
# Min Spanning Tree - Kruskal - Python
def mst_kruskal(
    node: List[node], 
    edge: dict[node, List[node]],
    weight: dict[tuple[node, node], float]
):
    '''Data Structure - Disjoint Set'''
    parent = node[:]
    def get_root(x):
        if x != parent[x]:
            parent[x] = get_root(parent[x])
        return parent[x]
    def unify_root(x, y):
        x, y = get_root(x), get_root(y)
        if x != y:
            parent[y] = x

    '''Kruskal Implement'''
    edge = sorted(edge, key=lambda e: weight[e[0]][e[1]], reverse=True)
    mst = []

    # while MST not done...
    while len(mst) < len(node) - 1:
        # get minimum weight edge...
        v, w = edge.pop()
        
        # check if it makes cycle...
        if get_root(v) != get_root(w):
            # if not, take it into MST
            mst.append((v, w))
            unify_root(v, w)
    
    return mst
```

### Network Flow (TODO)

#### Ford-Fulkerson (TODO)

#### Bipartite Matching (TODO)

## Geometry (TODO)

## Numeric Analysis (TODO)

<!--

# 3부 알고리즘 설계 패러다임
    ## 11장 조합 탐색
    ## 12장 최적화 문제 결정 문제로 바꿔 풀기

# 4부 유명한 알고리즘들
    ## 13장 수치 해석
    ## 14장 정수론
    ## 15장 계산 기하

# 5부 기초 자료 구조
    ## 16장 비트마스크
    ## 17장 부분 합
    ## 18장 선형 자료 구조
    ## 19장 큐와 스택, 데크
    ## 20장 문자열

# 6부 트리
    ## 21장 트리의 구현과 순회
    ## 22장 이진 검색 트리
    ## 23장 우선순위 큐와 힙
    ## 24장 구간 트리
    ## 25장 상호 배타적 집합
    ## 26장 트라이

# 7부 그래프
    ## 27장 그래프의 표현과 정의
        ## 28장 그래프의 깊이 우선 탐색
        ## 29장 그래프의 너비 우선 탐색
    ## 30장 최단 경로 알고리즘
        ### 30.9 벨만-포드 알고리즘
        ### 30.12 플로이드-워셜 알고리즘
    ## 31장 최소 스패닝 트리
        ### 31.3 프림의 최소 스패닝 트리 알고리즘
    ## 32장 네트워크 유량
        ### 32.2 포드-풀커슨 알고리즘
        ### 32.3 네트워크 모델링
        ### 32.8 이분 매칭

* **단일** 출발, **전체** 도착 (= 다익스트라)
* 음수 cycle 탐지 가능
* 암기: Bellman-Ford (B-etter)
* 시작 노드 1개에 대해 $O(VE)$

```python
def get_shortest(node_count, edge, start):
    dist = [float("inf")] * node_count
    dist[start] = 0
    
    # 총 V번의 갱신 시도
    for step in range(1, node_count + 1):
        # 각 갱신마다 모든 edge 체크
        for start, end, weight in edge:
            # 개척 노드만 따지자...
            if dist[start] != float("inf"):
                continue 

            # 만약 (더 나은 개척로가 있다면) -> 갱신
            new_dist = dist[start] + weight
            if dist[end] > new_dist:
                dist[end] = new_dist

                # V번째 갱신이 성공한 거면: 음수사이클 존재 (망했어요)
                if step == node_count - 1:
                    return None

    return dist
```

* **전체** 출발, **전체** 도착
* 음수 cycle 탐지 가능
* 암기: Floyd-Warshall (F-ull)
* 시작 노드 $V$개에 대해 $O(V^3)$

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
-->