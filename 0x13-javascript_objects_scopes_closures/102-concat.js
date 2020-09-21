#!/usr/bin/node
// concatenate 2 files
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const w = fs.createWriteStream(fileC, { flags: 'a' });
const r1 = fs.createReadStream(fileA);
r1.pipe(w);
const r2 = fs.createReadStream(fileB);
r2.pipe(w);
