#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1,2,3,4,5,7};
    try {
        v.at(19);
    }
    catch(out_of_range e) {
        cout << "Caught: " << e.what();
    }
    return 0;
}