#!/usr/bin/node
// imports a dict and computes a dict by ocurrences
const dict = require('./101-data').dict;
const newDict = {};
let lista = [];
for (const [key, value] of Object.entries(dict)) {
  if (!(value in newDict)) {
    lista = [];
  } else {
    lista = newDict[value];
  }
  lista.push(key);
  newDict[value] = lista;
}
console.log(newDict);
