#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let x = list.length - 1; x >= 0; x--) {
    revList.push(list[x]);
  }
  return revList;
};
