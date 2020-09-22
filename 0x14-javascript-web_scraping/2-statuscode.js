#!/usr/bin/node
// display the status code of a get request
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
