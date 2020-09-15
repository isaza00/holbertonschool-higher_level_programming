#!/usr/bin/node
// prints two arguments separeted by "is"
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
