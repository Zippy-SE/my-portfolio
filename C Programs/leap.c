#include <stdio.h>
#include "leap.h"

bool leap_year(int year) {
    if (year % 400 == 0) {
        return true;
    } else if (year % 100 == 0) {
        return false;
    } else if (year % 4 == 0) {
        return true;
    } else {
        return false;
    }
}

int main(void) {
    int year;

    printf("Enter a year: ");
    scanf("%d", &year);

    if (leap_year(year)) {
        printf("%d is a leap year.\n", year);
    } else {
        printf("%d is not a leap year.\n", year);
    }

    return 0;
}