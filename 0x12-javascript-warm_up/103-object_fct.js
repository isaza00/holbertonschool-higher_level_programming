#!/usr/bin/node
// update this script adding a new function incr that increments value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
