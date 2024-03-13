#!/usr/bin/node
const dict = require('./101-data').dict;

let valList =  Object.entries(dict)
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
    }
  }
console.log(out)
