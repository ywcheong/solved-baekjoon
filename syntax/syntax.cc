#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef long long bigint;
const char eol = '\n';

int main() {
    // Desync stdio w/ iostream + Desync cin/cout
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // ==========================
    // Basic Types & Operations
    // ==========================

    int my_integer = 3;
    bigint my_long = 987654321012;
    double my_float = 3.4;

    // Integer Arithmetic
    cout << my_integer + 4 << eol;
    cout << my_long + 4 << eol;
    cout << my_float + 4 << eol;
    cout << my_integer << eol;
    cout << 3 - 4 << eol;
    cout << 3 * 4 << eol;
    cout << 4 / 3 << eol;
    cout << 4 % 3 << eol;

    // Casting
    cout << static_cast<float>(4) / 3 << eol;
    cout << static_cast<float>(4) / 3 << eol;

    // Bit operation
    cout << (int)(0b0111 & 0b1100) << eol;
    cout << (int)(0b0111 | 0b1100) << eol;

    // ======================
    // Input & Output
    // ======================

    int input_a, input_b;
    cin >> input_a;             // Can read `1`
    cin >> input_a >> input_b;  // Can read `1 2`

    string str_a, str_b;
    cin >> str_a >> str_b;  // Can read `hello world`

    // `cin >> value` 꼴을 사용한 뒤
    // getline(cin, string)을 사용하려면
    // 반드시 cin.ignore()을 선행시킬 것
    // 그 외에는 사용 X
    string string_with_space;
    cin.ignore();
    getline(cin, string_with_space);  // Can read "this is long text"

    cout << eol
         << "Floating Point Precision" << eol;
    cout << setprecision(5) << 40.0 / 3 << eol;           // AA.BBB
    cout << fixed << setprecision(5) << 40.0 / 3 << eol;  // AA.BBBBB

    // ======================
    // String
    // ======================

    string my_str;
    string my_str2 = "abc";
    string my_str3(my_str2);
    cout << (my_str2.find("a") == 0) << eol;
    cout << (my_str2.find("what the heck") == string::npos) << eol;
    my_str2 += "efg";
    my_str2[2] = 'k';

    // ======================
    // Vector
    //  - dynamic array
    // ======================

    vector<int> listA = {1, 2, 3, 4, 5};
    vector<bool> listB(100, false);  // [False, ..., False] // ListB[100] = False처럼 암기...
    vector<int> listC(listA);
    vector<int> listD(100);  // [???, ???, ..., ???] (length = 100)

    // N-Dimensional Array
    int row = 3, column = 4;
    int init_value = 0;
    vector<vector<int>> board(row, vector<int>(column, init_value));
    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 6, 7},
        {8, 9, 10, 11, 12},
    };

    // Push/pop
    listA.push_back(6);
    listA.pop_back();

    // Insert at front !!! WARNING: TIME COMPLEXITY O(n)) !!!
    listA.insert(listA.begin(), -100);

    // ======================
    // Set
    //  - Set: Binary Tree
    // ======================
    // #include <set>
    set<int> S = {4, 3, 1, 3, 2};  // {1, 2, 3, 4}
    auto it = S.find(4);           // Find: (*it == 4)
                                   // Not found: (it == S.end())

    S.insert(7);
    S.erase(it);  // Both pointer
    S.erase(3);   // and value works

    // ======================
    // Map
    //  - Map: Binary Tree
    // ======================
    map<string, int> student_score;
    student_score = {
        {"John Smith", 34},
        {"Ela Mena", 24},
    };

    student_score["John Doe"] = 33;                                          // New Key
    cout << (student_score.find("John Doe") == student_score.end()) << eol;  // Is Key in?

    // ======================
    // Unordered Set, Map
    //  - Set, Map: Hash
    // ======================

    // Same as set, map

    // ======================
    // Closure
    //  - First Class Function
    //  - Check closure.cc
    // ======================

    // ======================
    // Algorithm
    //  - Useful functions
    // ======================
    vector<int> M = {1, 2, 3, 4, 5};
    cout << count(M.begin(), M.end(), 3) << eol;
    cout << count_if(M.begin(), M.end(), [](int x) { return x >= 3; }) << endl;

    sort(M.begin(), M.end());   // Sort asc
    sort(M.rbegin(), M.rend()); // Sort desc
    sort(M.begin(), M.end(), [](int left, int right) -> bool { return left < right; } );    // Custom compare function of LE (<)

    

    return 0;
}