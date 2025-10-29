#include <stdio.h>
#include <stdlib.h>

int main() {
    
    printf("The number %d is an integer.\n",127);
    printf("The number %1.2f is a float.\n",3.1415926535);
    printf("The number %d is an integer.\n",122013);
    printf("The number %1.1f is a float.\n",0.00008);

    // Pause so the console stays open when launched from VS Code or an external terminal
    printf("\nPress Enter to exit...");
    fflush(stdout);
    getchar();

    return (0);
}