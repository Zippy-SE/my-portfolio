#include <iostream>
using namespace std;

int main() {
    int ages[5];
    int min = 0;
    double total = 0;

    for (int i = 0; i < 5; ++i) {
        cin >> ages[i];

        if (i == 0) {
            min = ages[i];
        } else if (ages[i] < min) {
            min = ages[i];
        }
    }

total = 50 - 50 * (double(min) / 100);
cout << total << endl;


return 0;
    
    


    
}