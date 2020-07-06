/*
A program to calulate the largest prime
factor of 600851475143

Author: Lucas Gracia
URL www.lucasgracia.com
Date: 2017-08-24
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[]) {
  clock_t begin = clock();                                                      //Capture start time
  long long number = 600851475143, divisor = 2, ans = 0, factor;                //Store the number and declare used variables

  while (number != 0){
    if (number % divisor != 0){                                                 //If divisor doesn't evenly divide into number
      divisor += 1;                                                             //Move to the next divisor
    }else{
      factor = number;                                                          //Divide the number by the discovered divisor
      number = number / divisor;                                                //and repeat the process

      if (number == 1){
        clock_t end = clock();                                                  //Capture end time
        double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;             //Calculate time_taken
        printf("Answer: %d\n\nTime Taken:%lf seconds", factor, time_taken);     //Print answer
        ans = 1;
        break;
      }
    }
  }







  return 0;
}
