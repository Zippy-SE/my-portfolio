#include <stdio.h>

int main(void) {
    int x = 0;
    int y = 0;

    printf("Enter a number for x.");
    scanf("%d", &x);
    printf("Enter a number for y.");
    scanf("%d", &y);

    if (x < y) {
        printf("x is less than y");
    } else if (x > y) {
        printf("x is greater than y");
    } else {
        printf("x is equal to y");
    }
    return 0;
}