#!/usr/bin/node
// print number of films of character 18
const request = require('request');
let url = process.argv[2];
url = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) return console.error('error:', error);
  console.log(JSON.parse(body).films.length);
});
