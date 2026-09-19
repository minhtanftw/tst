#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v1;

    vector<int> v2(3,6);

    for (int x : v2){
        cout << x << " ";
    }
    cout << endl;

    vector<int> v3 = { 1,2,34,5,6,7,8};

    for(int x : v3){
        cout << x << " ";
    }
}