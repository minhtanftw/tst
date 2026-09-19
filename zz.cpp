#include <iostream>
#include <queue>
using namespace std;


int main() {
    queue<int>q;
    q.push(3);
    q.push(2);
    q.push(12);
    queue<int> temp(q);
    while(!temp.empty()){
        cout << temp.front() << " ";
        temp.pop();
    }

    try{
        throw 10;
    }
   /* catch(int e) {
        std::cout <<"Error:" << e << endl;
    } */
    catch(const char *e){
        std::cout << "String error";
    }

    return 0;
}