#!/usr/bin/node
// if w or h is equal to 0 or not positibe create empty obj
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
