// My Solution : https://github.com/ywcheong/solved-baekjoon

// Essential Headers
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

typedef long long bigint;
const char eol = '\n';
const int INF = 987654321;

int solve(const string& original, const string& target) {
    int olen = original.length(), tlen = target.length();
    vector<vector<int>> memo(olen + 1, vector<int>(tlen + 1, -1));

    for (int o_sublen = 0; o_sublen <= olen; ++o_sublen) {
        for (int t_sublen = 0; t_sublen <= tlen; ++t_sublen) {
            int result;

            if (o_sublen == 0) {
                result = (t_sublen == 0) ? 0 : 1;
            } else {
                char o_char = original[o_sublen - 1];
                result = INF;

                for (int t_index = 0; t_index < t_sublen; ++t_index) {
                    char t_char = target[t_index];

                    if (o_char == t_char) {
                        int this_result = memo[o_sublen - 1][t_index];

                        if (t_index < t_sublen - 1) {
                            ++this_result;
                        }

                        result = min(result, this_result);
                    }
                }
            }

            memo[o_sublen][t_sublen] = result;
        }
    }

    int output = memo[olen][tlen];
    return (output == INF) ? -1 : output;
}

void test() {
    auto check = [](int left, int right) {
        if (left == right) {
            cout << "Test pass" << eol;
        } else {
            cout << "Test fail: " << left << " != " << right << eol;
        }
    };

    check(solve("hello fine", "hello, how are you? I'm fine thank you and you?"), 2);
    check(solve("aaaaa", "ababababa"), 4);
    check(solve("no way", "No way!"), -1);
    check(solve("abcefijklmnopuvwxz", "abcdefghijklmnopqrstuvwxyz"), 4);
    check(solve("B", "ABC"), 2);
    check(solve("A", "ABC"), 1);
    check(solve("C", "ABC"), 1);
    check(solve("C", "ABCDE"), 2);
    check(solve("", ""), 0);
    check(solve("A", ""), -1);
    check(solve("", "A"), 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string original, target;
    getline(cin, original);
    getline(cin, target);
    cout << solve(original, target) << eol;

    // Uncomment the following line to run tests
    // test();

    return 0;
}
