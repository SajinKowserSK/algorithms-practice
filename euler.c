/**
SM Shahariar Kowser | 251014520
This is euler.c 
**/

#include <stdio.h>
#include <stdlib.h>

// recursive helper function factorial takes integer and calculates its factorial
double factorial (double integer){

  // break case if integer is 0, factorial of 0 is 1
  if (integer == 0){
    return 1;
  }

  // recursive case which is integer * factorial(number before it)
  else{
    return integer * factorial(integer-1);
  }
}

int main()
{   

    double user_input;

    // n is of type long long as it has more memory allocated to it, can hold 
    // more digits than of type int
    long long n = 0;

    // keeps prompting user if number smaller or equal to 0 is entered
    do {
       printf("Please enter a small number greater than 0:\n");
       scanf("%lf", &user_input);
    }

    while(user_input <= 0);

    // isolating original asn equation for n 
    // this while loop computes smallest integer n such that 1/n! <= e 
    while (1/user_input >= factorial(n)){
        n++;
    }

    // initializing first val to 1 before adding the 1/factorials
    double euler = 1;
    while (n > 0){
      euler = euler + (1 / factorial(n));
      n--;
    }

    // returning approximate result
    printf("Value of e: %.15lf\n", euler);
}


