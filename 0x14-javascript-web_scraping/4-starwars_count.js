#!/usr/bin/node
// print number of films of character 18
const request = require('request');
const url = process.argv[2];
let sum = 0;
request(url, function (error, response, body) {
  if (error) return console.error('error:', error);
  for (const item of JSON.parse(body).results) {
    for (const uri of item.characters) {
      if (uri === 'https://swapi-api.hbtn.io/api/people/18/') {
        sum += 1;
      }
    }
  }
  console.log(sum);
});
