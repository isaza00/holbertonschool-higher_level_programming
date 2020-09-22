#!/usr/bin/node
// print starwars movie title where episode id is given
const request = require('request');
const idTitle = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + idTitle;
request(url, function (error, response, body) {
  if (error) return console.error('error:', error);
  console.log(JSON.parse(body).title);
});
