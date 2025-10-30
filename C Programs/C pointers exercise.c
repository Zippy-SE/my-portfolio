#include <stdio.h>
#include <stdlib.h>

int main () {
    int **ramon;
    int *paul;
    int melissa = 5;
    paul = &melissa;
    ramon = &paul;
    
    printf("ramon = %d\n", ramon);
    printf("&paul = %d\n", &paul);
    printf("*ramon  = %d\n", *ramon);
    printf("&melissa = %d\n", &melissa);
    printf("**ramon = %d\n", **ramon);

    system("pause");
        
    return (0);
}