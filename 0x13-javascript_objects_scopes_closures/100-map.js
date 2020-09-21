#!/usr/bin/node
// imports array and map to another array
const list = require('./100-data').list;
console.log(list);
console.log(list.map((item, index) => item * index));
