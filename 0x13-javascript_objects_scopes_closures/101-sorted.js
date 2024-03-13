#!/usr/bin/node
const dict = require('./101-data').dict;

const valList = Object.entries(dict);
const out = {};
while (valList.length) {
  const curVal = valList[0][1];
  for (const member of valList) {
    const [key, value] = member;
    if (value === curVal) {
      if (key in out) {
        out[curVal].push(key);
      } else {
        out[curVal] = [];
        out[curVal].push(key);
      }
      valList.splice(valList.indexOf(member), 1);
    }
  }
}
console.log(out);
