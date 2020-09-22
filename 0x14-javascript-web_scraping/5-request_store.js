#!/usr/bin/node
// gets content of webpage and save it to file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
request(url).pipe(fs.createWriteStream(file));
