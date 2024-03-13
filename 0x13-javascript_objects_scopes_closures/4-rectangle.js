#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let m = '';
        for (let x = 0; x < this.width; x++) { m += 'X'; }
        console.log(m);
      }
    }
  rotate() {
    [this.width, this.height] = [this.height, this.width]
  }
  double() {
    this.height *= 2;
    this.width *=2;
  }
  }
