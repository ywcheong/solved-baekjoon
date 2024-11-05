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
// #include <queue>         // Queue, Priority Queue
// #include <deque>         // Deque

// // Ready-to-use
// // * multi~ (ex. unordered_multiset)
// #include <set>           // Sorted BTree, element
// #include <map>           // Sorted BTree, key-value
#include <unordered_set>  // Hash Table, element
// #include <unordered_map> // Hash Table, key-value

using namespace std;

// Keystroke-saving hacking: do not use in real world
typedef long long bigint;
const char eol = '\n';

void backtrack(
    vector<vector<int>>& board,
    vector<bool>& available_rows,
    int& known_max,
    int col,
    int npress) {
    // cout << known_max << " / " << col << " / " << npress << eol;

    if (static_cast<size_t>(col) == board[0].size()) {
        if (npress % 2 == 0) {
            int current_count = count(available_rows.begin(), available_rows.end(), true);
            known_max = known_max > current_count ? known_max : current_count;
        }
        return;
    }

    auto press_row = [&board, &available_rows, &col](bool is_press) -> vector<int> {
        vector<int> opt_out;
        for (size_t row = 0; row < board.size(); row++) {
            if (!(board[row][col] ^ is_press)) {
                available_rows[row] = false;
                opt_out.push_back(row);
            }
        }
        return opt_out;
    };

    auto unpress_row = [&available_rows](const vector<int>& opt_out) -> void {
        for (auto row : opt_out)
            available_rows[row] = true;
    };

    for (bool is_press : {true, false}) {
        if (npress == 0 && is_press)
            continue;

        vector<int> opt_out = press_row(is_press);

        if (count(available_rows.begin(), available_rows.end(), true) > known_max) {
            backtrack(
                board,
                available_rows,
                known_max,
                col + 1,
                is_press ? npress - 1 : npress);
        }

        // choice deapplying
        unpress_row(opt_out);
    }
}

int main() {
    // Desync stdio w/ iostream + Desync cin/cout
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Write your code here
    int nrow, ncolumn;
    cin >> nrow >> ncolumn;
    vector<vector<int>> board(nrow, vector<int>(ncolumn, 0));
    cin.ignore();

    for (auto& row : board) {
        string row_input;
        getline(cin, row_input);

        for (size_t j = 0; static_cast<int>(j) < ncolumn; j++) {
            row[j] = (row_input[j] == '1') ? 1 : 0;
        }
    }

    int npress;
    cin >> npress;

    vector<bool> available_rows(nrow, true);
    int known_max = 0;

    backtrack(board, available_rows, known_max, 0, npress);
    cout << known_max << eol;

    return 0;
}