#!/usr/bin/node
// converts a number from base 10 to anogher base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
