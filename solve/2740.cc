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
    int N, M;
    cin >> N >> M;
    vector<vector<int>> A(N, vector<int>(M, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> A[i][j];
        }
    }

    int _dump, K;
    cin >> _dump >> K;
    vector<vector<int>> B(M, vector<int>(K, 0));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < K; j++) {
            cin >> B[i][j];
        }
    }

    vector<vector<int>> C(N, vector<int>(K, 0));
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < K; c++) {
            for (int pos = 0; pos < M; pos++) {
                C[r][c] += A[r][pos] * B[pos][c];
            }

            if (c != 0)
                cout << " ";
            cout << C[r][c];
        }
        cout << eol;
    }

    return 0;
}