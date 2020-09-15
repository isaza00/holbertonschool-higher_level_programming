#!/usr/bin/node
// prints a square of X
let size = process.argv.slice(2)[0];
size = parseInt(size);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let string = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      string += 'X';
    }
    console.log(string);
    string = '';
  }
}
