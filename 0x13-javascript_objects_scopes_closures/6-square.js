#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let m = '';
      for (let x = 0; x < this.size; x++) { m += c; }
      console.log(m);
      }
    }
  }

module.exports = Square;
