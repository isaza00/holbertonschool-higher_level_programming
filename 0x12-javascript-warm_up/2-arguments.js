#!/usr/bin/node
// prints a message depending of number of arguments passed
const numberArgs = process.argv.slice(2).length;
if (numberArgs === 0) {
  console.log('No argument');
} else if (numberArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
