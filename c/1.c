/*
A program to find the sum of all multiples
of 3 and 5 below 1000

Author: Lucas Gracia
Date: 2017-08-24
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[]) {

  int sum = 0;                                                                  
  clock_t begin = clock();                                                      

  for (int i = 1; i < 1000; i++){                                               
    if (i % 3 == 0 || i % 5 == 0){                                              
      sum += i;                                                                 
    }
  }

  clock_t end = clock();                                                        
  double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;                   
  printf("%d\n\nTime Taken:%lf seconds", sum, time_taken);                      

  return 0;
}