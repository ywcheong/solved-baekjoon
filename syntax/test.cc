#include <string>
#include <iostream>
#include <vector>
using namespace std;

const char EOL = '\n';

int main(){
    int n;
    cin >> n;

    vector<string> L(n);
    for(int i = 0; i < n; i++){
        cin >> L[i];
    }

    cout << "answer" << EOL;

    for(auto str : L){
        cout << str << EOL;
    }
}