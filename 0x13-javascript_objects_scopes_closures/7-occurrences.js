#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (const x of list) {
    if (searchElement === x) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
