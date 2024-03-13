#!/usr/bin/node
exports.esrever = function (list) {
  const Revlist = [];
  for (let x = list.length - 1; x >= 0; x--) {
    Revlist.push(list[x]);
  }
  return list;
};
