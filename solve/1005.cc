// My Solution : https://github.com/ywcheong/solved-baekjoon

// Essential Headers
#include <algorithm>  // count, count_if, sort, ...
#include <iomanip>    // cin << fixed << setprecision
#include <iostream>   // cin(ignore/getline), cout
#include <sstream>    // stringstream.str()
#include <string>     // string
#include <vector>     // vector

// // Common Data Structure
// #include <forward_list>  // Single Linked List
// #include <list>          // Double Linked List
// #include <stack>         // Stack
#include <queue>  // Queue, Priority Queue
// #include <deque>         // Deque

// // Ready-to-use
// // * multi~ (ex. unordered_multiset)
// #include <set>           // Sorted BTree, element
// #include <map>           // Sorted BTree, key-value
// #include <unordered_set> // Hash Table, element
#include <unordered_map>  // Hash Table, key-value

// Include Extra header here

using namespace std;

// Keystroke-saving hacking: do not use in real world
typedef long long bigint;
const char eol = '\n';

struct Edge {
    int weight;
    int next;
    Edge(int weight, int next) : weight(weight), next(next) {}
};

struct NextVisit {
    int dist;
    int node;
    NextVisit(int dist, int node) : dist(dist), node(node) {}
    bool operator<(const NextVisit& other) const {
        return this->dist < other.dist;
    }
};

bigint compute_shortest(int starting, unordered_map<int, vector<Edge>>& rule_list) {
    queue<NextVisit> to_visit;
    unordered_map<int, int> visited;
    bigint result = 0;

    to_visit.push(NextVisit(0, starting));
    visited[starting] = 0;

    while (!to_visit.empty()) {
        auto [dist, v] = to_visit.front();
        to_visit.pop();

        // 만료된 노드 제거
        if (dist > visited[v]) {
            continue;
        }

        // 엣지로 연결된 노드 탐색
        for (auto [weight, w] : rule_list[v]) {
            int new_dist = dist + weight;
            // 미방문이거나 or 더 나은 개척로
            if (visited.find(w) == visited.end() || visited[w] > new_dist) {
                visited[w] = new_dist;
                to_visit.push(NextVisit(new_dist, w));
                result = min(result, static_cast<bigint>(new_dist));
            }
        }
    }

    return -result;
}

int main() {
    // Desync stdio w/ iostream + Desync cin/cout
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Write your code here
    int testcase_count;
    cin >> testcase_count;
    for (int test_id = 0; test_id < testcase_count; test_id++) {
        int build_count, rule_count;
        cin >> build_count >> rule_count;

        // Get Build List
        vector<int> build_list(build_count);
        for (auto& element : build_list) {
            cin >> element;
        }

        // Prepare RuleBook
        unordered_map<int, vector<Edge>> rule_list;
        for (int node = 1; node < build_count + 1; node++) {
            rule_list[node] = vector<Edge>();
        }

        // Record Rules
        for (int _ = 0; _ < rule_count; _++) {
            int start, end;
            cin >> start >> end;
            rule_list[end].push_back(Edge(-build_list[start - 1], start));
        }

        int target_building;
        cin >> target_building;
        cout << compute_shortest(target_building, rule_list) + build_list[target_building - 1] << eol;
    }

    return 0;
}