#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) return console.error(error);
  const list = JSON.parse(body);
  const dict = {};
  for (const item of list) {
    if (!(item.userId in dict)) {
      dict[item.userId] = 0;
    }
    if (item.completed === true) {
      dict[item.userId] += 1;
    }
  }
  return console.log(dict);
});
