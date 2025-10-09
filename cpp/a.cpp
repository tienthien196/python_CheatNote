#include <iostream>

using namespace std;


int main(){
    int a[100] = {1,4,5,67,3};
    int b[100];
    
    
    std::copy(a, a + 5, b);
    cout <<a<<endl;

    return 0;
}
