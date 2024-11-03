#include <iostream>
#include <vector>
using namespace std;

int main() {
    int b = 100;

    auto myClosure = [](int a) -> int {
        return a + 10;
    };

    auto myClosureValueCapture = [b](int a) {
        return a + b;
    };

    auto myClosureValueCaptureMutable = [b](int a) mutable {
        b = 1000;   // Note that does NOT affect outside
        return a + b;
    };

    auto myClosureReferenceCapture = [&b](int a) {
        b = 1000;   // Note that does YES affect outside
        return a + b;
    };

    auto dangerousClosure = [](int a) -> vector<int>* {
        vector<int> L = {1, 2, 3, a};
        return &L;  // DANGLING POINTER
    };

    cout << "myClosure " << myClosure(1) << endl;
    cout << "myClosureValueCapture " << myClosureValueCapture(1) << endl;
    cout << "myClosureValueCaptureMutable " << myClosureValueCaptureMutable(1) << endl;
    cout << "b " << b << endl;
    cout << "myClosureReferenceCapture " << myClosureReferenceCapture(1) << endl;
    cout << "b " << b << endl;

    vector<int>* dangerList = dangerousClosure(9);
    // cout << "dangerousClosure " << (*dangerList)[3] << endl; // SegFault

    return 0;
}