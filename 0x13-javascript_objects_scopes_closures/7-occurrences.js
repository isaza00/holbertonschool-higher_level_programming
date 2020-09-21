#!/usr/bin/Node
// function that returns number of ocurrencies
exports.nbOccurences = function (list, searchElement) {
  if (Array.isArray(list)) {
    let occurrences = 0;
    for (let i = 0; i < list.length; i++) {
      if (searchElement === list[i]) {
        occurrences += 1;
      }
    }
    return occurrences;
  }
};
