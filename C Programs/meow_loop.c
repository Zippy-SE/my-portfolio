#include <stdio.h>

int main(void) {
    printf("Choose a number: ");
    int num;
    scanf("%d", &num);

    for (int i=0; i < num; i++) {
        printf("meow!\n");
    }
    return 0;
}
