'use strict';

class Sharpie {
    constructor (color, width) {
    this.sharpieColor = color;
    this.sharpieWidth = width;
    this.inkAmount = 100;
    }
    use() {
        while (this.inkAmount > 0) {
            this.inkAmount -= this.sharpieWidth;
        }
        if (this.inkAmount < 0){
            this.inkAmount = 0;
        }
    }
}

var sharpieOne =  new Sharpie('blue', 30);

console.log(sharpieOne.sharpieColor);
console.log(sharpieOne.inkAmount);

sharpieOne.use();

console.log(sharpieOne.inkAmount);