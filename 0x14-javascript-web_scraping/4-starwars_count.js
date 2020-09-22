#!/usr/bin/node
// print number of films of character 18
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';
let sum = 0;
request(url, function (error, response, body) {
  if (error) return console.error('error:', error);
  for (const item of JSON.parse(body).results) {
    if (item.characters.includes(character)) {
      sum += 1;
    }
  }
  console.log(sum);
});
