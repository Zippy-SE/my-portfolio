#include <stdio.h>
#include <stdlib.h>

int main() {
    //Exercise 5-5
    printf("The result of adding 456.98 and 213.4 is %1.2f\n", 456.98 + 213.4);
    printf("The result of subtracting 456.98 and 213.4 is %1.2f\n", 456.98 - 213.4);
    //Exercise 5-6    
    printf("The result of multiplying 8, 14, and 25 is %d\n", 8 * 14 * 25);
    //Exercise 5-7
    printf("What is this mathematical riddle: 0 + 50 x 1 - 60 - 60 * 0 + 10? %d\n", 0 + 50 * 1 - 60 - 60 * 0 + 10);
    system("pause");
    return (0);
}