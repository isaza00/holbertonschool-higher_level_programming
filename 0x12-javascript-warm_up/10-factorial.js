#!/usr/bin/node
// computes and prints factorial
let number = process.argv.slice(2)[0];
number = parseInt(number);
function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return 1;
  }
  return number * factorial(number - 1);
}
console.log(factorial(number));
