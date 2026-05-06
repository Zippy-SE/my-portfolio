#include <stdio.h>
int main()
{
    int c;
    int d, e, f;

    //getchar() example with a loop that clears the new line buffer for the following getc() function below this one
    printf("I'm waiting for a character: ");
    while ((c = getchar()) != '\n' && c != EOF) {
        printf("I waited for the '%c' character.\n", c);
        printf("I choose '%d', an ASCII value instead!\n", c);
    }
    
     
    // Alternate getc() example
    printf("Enter three characters: ");
    d = getc(stdin);
    e = getc(stdin);
    f = getc(stdin);

    printf("You entered:\n '%c', '%c', '%c'\n", d, e, f);

    return 0;
}