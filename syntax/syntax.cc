#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

typedef long long bigint;

int main(){
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
    cout << my_integer + 4 << '\n';
    cout << my_long + 4 << '\n';
    cout << my_float + 4 << '\n';
    cout << my_integer << '\n';
    cout << 3 - 4 << '\n';
    cout << 3 * 4 << '\n';
    cout << 4 / 3 << '\n';
    cout << 4 % 3 << '\n';

    // Casting
    cout << static_cast<float>(4) / 3 << '\n';
    cout << static_cast<float>(4) / 3 << '\n';

    // Bit operation
    cout << (int) (0b0111 & 0b1100) << '\n';
    cout << (int) (0b0111 | 0b1100) << '\n';

    // ======================
    // Input & Output
    // ======================

    int input_a, input_b;
    cin >> input_a;             // Can read `a`
    cin >> input_a >> input_b;  // Can read `a b`
    


    cout << '\n' << "Floating Point Precision" << '\n';
    cout << setprecision(5) << 40.0 / 3 << '\n'; // AA.BBB
    cout << fixed << setprecision(5) << 40.0 / 3 << '\n'; // AA.BBBBB


    return 0;
}