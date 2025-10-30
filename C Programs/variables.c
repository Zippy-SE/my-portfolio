#include <stdio.h>

main ()
{
    float salary, taxowed;
    printf ("How much money did you make last year? ");
    scanf ("%f", &salary);
    taxowed = salary * 0.95;
    printf ("This is how much tax you owe =  %8.2f", taxowed);
}