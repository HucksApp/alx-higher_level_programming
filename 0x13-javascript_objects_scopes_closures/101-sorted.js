#!/usr/bin/node
const dict = require('./101-data').dict;

let valList =  Object.entries(d)
let out = {}
  while (valList.length) {
    const cur_val = valList[0][1];
    for (let member of valList) {
        const [key, value] = member;
        if (value === cur_val) {
            if(key in out){
                out[cur_val].push(key)
            }
            else {
                out[cur_val] = []
                out[cur_val].push(key)
            }
            valList.splice(valList.indexOf(member), 1)
        } 
    }
  }
console.log(out)
