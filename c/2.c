/*
A program to calculate the sum of all even
fibonacci numbers less than 4,000,000

Author: Lucas Gracia
Date: 2017-08-24
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char const *argv[]) {
  clock_t begin = clock();                                                      
  int previousTerm = 1;
  int currentTerm = 1;                                                              
  int nextTerm = 0;                                                               
  int runningTotal = 0;

  while (nextTerm < 4000000){                                                     
    if (nextTerm % 2 == 0){                                                       
      runningTotal += nextTerm;                                                          
    }
     nextTerm = currentTerm + previousTerm;                                               
     previousTerm = currentTerm;
     currentTerm = nextTerm;
  }

  clock_t end = clock();                                                        
  double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;                   

  printf("%d\n\nTime Taken:%lf seconds", runningTotal, time_taken);                    

  return 0;
}