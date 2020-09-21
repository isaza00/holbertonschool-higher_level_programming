#!/usr/bin/node
// add method prints square
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
      string = '';
    }
  }
};
