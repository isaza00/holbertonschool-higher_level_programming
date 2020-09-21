#!/usr/bin/node
// class square inherits from rectangle
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size = 0) {
    super(size, size);
  }
};
