#!/usr/bin/node
// prints number of arguments already printed
let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num += 1;
};
