#include <iostream>
using namespace std;

int main() {
    string hello = "Hello";
    int values[] = {1, 2, 3, 4, 5, 0};

    // Auto data type is used to automatically deduce the type of a variable from its initializer.
    for (int i = 0; auto c = hello[i]; i++) {
        cout << c << " ";
    }

    cout << endl;
    
    // Same idea as above but with an array of integers. The loop will stop when it reaches the null terminator (0) at the end of the array.
    for (int i = 0; auto v = values[i]; i++) {
        cout << v << " ";
    }

    return 0;
}