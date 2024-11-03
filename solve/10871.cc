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

// Include Extra header here
// #include <

using namespace std;

// Keystroke-saving hacking: do not use in real world
typedef long long bigint;
const char eol = '\n';

int main() {
    // Desync stdio w/ iostream + Desync cin/cout
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Write your code here
    int number_count, bound;
    cin >> number_count >> bound;

    vector<int> number_list(number_count);
    for (auto& element : number_list) {
        cin >> element;
    }

    bool is_first = true;
    for (auto element : number_list) {
        if (element < bound){
            if (!is_first)
                cout << " ";
            cout << element;
            is_first = false;
        }
    }

    cout << eol;

    return 0;
}