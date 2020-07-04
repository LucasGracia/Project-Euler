/*
 * Solution to Project Euler Problem 3
 *
 * The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
 * factor of the number 600851475143 ?
 */
function isPrime (x) {
  for (var i = 2; i < x; i++) {
    if (x % i === 0) {
      return false
    }
  }
  return true
}

let number = 600851475143
let divisor = 2
let primeFactors = []
while (number > 1) {
  if (isPrime(divisor)) {
    if (number % divisor === 0) {
      primeFactors.push(divisor)
      number = number / divisor
    } else {
      divisor++
    }
  } else {
    divisor++
  }
}
console.log(Math.max(...primeFactors))
