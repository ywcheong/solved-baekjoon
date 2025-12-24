// My Solution : https://github.com/ywcheong/solved-baekjoon

#include <algorithm>  // count, count_if, sort
#include <iomanip>    // fixed, setprecision
#include <iostream>   // cin(getline), cout
#include <sstream>    // stringstream.str()
#include <string>     // string
#include <vector>     // vector

// Special Data Structures
// #include <set>
// #include <map>
// #include <unordered_set>
// #include <unordered_map>
// #include <list>
// #include <stack>
#include <queue>

// Include Extra header here

using namespace std;

// Keystroke-saving hacking: do not use in real world
typedef long long bigint;
const char eol = '\n';

struct HeapElement {
    int value;
    HeapElement(int v) : value(v) {}
    bool operator<(const HeapElement& other) const {
        return this->value < other.value;
    }
};

int main() {
    // Desync stdio w/ iostream + Desync cin/cout
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Write your code here
    int n;
    cin >> n;
    priority_queue<HeapElement> heap;

    while (n-- > 0) {
        int input;
        cin >> input;

        if (input == 0) {
            if (heap.empty())
                cout << 0 << eol;
            else {
                cout << heap.top().value << eol;
                heap.pop();
            }
        } else {
            heap.push(HeapElement(input));
        }
    }

    return 0;
}