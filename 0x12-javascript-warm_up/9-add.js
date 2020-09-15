#!/usr/bin/node
// prints the addition of two numbers
const numbers = process.argv.slice(2);
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(numbers[0], numbers[1]);
