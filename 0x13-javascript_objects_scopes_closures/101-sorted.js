#!/usr/bin/node
const dict = require('./101-data').dict;

<<<<<<< HEAD
let valList =  Object.entries(d)
let out = {}
  while (valList.length) {
    const curVal = valList[0][1];
    for (let member of valList) {
        const [key, value] = member;
        if (value === curVal) {
            if(key in out){
                out[curVal].push(key)
            }
            else {
                out[curVal] = []
                out[curVal].push(key)
            }
            valList.splice(valList.indexOf(member), 1)
        } 
=======
const valList = Object.entries(d);
const out = {};
while (valList.length) {
  const cur_val = valList[0][1];
  for (const member of valList) {
    const [key, value] = member;
    if (value === cur_val) {
      if (key in out) {
        out[cur_val].push(key);
      } else {
        out[cur_val] = [];
        out[cur_val].push(key);
      }
      valList.splice(valList.indexOf(member), 1);
>>>>>>> :zap:
    }
  }
}
console.log(out);
