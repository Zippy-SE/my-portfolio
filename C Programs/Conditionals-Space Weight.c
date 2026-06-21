#include <stdio.h>

int main() {

int ew = 0;
int planetno = 0;

printf("What is your earth weight? ");
scanf("%d", &ew);

printf("Enter the number of the planet you would like to fight on? ");
scanf("%d", &planetno);

switch (planetno) {

  case 1: 
    printf("You have chosen Mercury.\n");
    double pw = ew * 0.38;
    printf("Your weight on Mercury is %.0f pounds\n", pw);
    break;

  default:
    printf("Please enter a valid planet number.");
  
}




return 0;


}