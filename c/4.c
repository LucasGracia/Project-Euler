/*
A program to calulate the largest palindrome
made from the product of two 3-digit numbers

Author: Lucas Gracia
URL www.lucasgracia.com
Date: 2017-08-24
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

//A function to determine if a number is a palindrome
int isPalindrome (int number){
  int remain, reverse = 0, temp = number;

  while (number > 0){
    remain = number % 10;
    reverse = reverse * 10 + remain;
    number /= 10;
  }

  if (temp == reverse){
    return 1;
  }else{
    return 0;
  }
}

int main(int argc, char const *argv[]) {
  clock_t begin = clock();                                                      //Capture start time
  int palindrome = 0, product = 0;

  for (int i = 0; i < 1000; i++){                                               //Two for loops calculate each possible product
    for (int j = 0; j < 1000; j++){                                             //of two 3-digit numbers less than 1000 before
      product = i * j;                                                          //passing that product to the isPalindrome
      if (isPalindrome(product)){                                               //function and storing the product if it is the largest
        if (product > palindrome){                                              //palindrome found so far.
          palindrome = product;
        }
      }
    }
  }

  clock_t end = clock();                                                        //Capture end time
  double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;                   //Calculate time_taken

  printf("Answer: %d\n\nTime Taken:%lf seconds", palindrome, time_taken);       //Print the result and the time taken

  return 0;
}
