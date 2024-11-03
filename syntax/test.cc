#include <iostream>
#include <string>
using namespace std;

int main()
{
    int val1, val2;
    string str;
    cin >> val1;
    cin >> val2;
    cin.ignore();
    getline(cin, str);
    cout << val1 << val2 << str << endl;

}