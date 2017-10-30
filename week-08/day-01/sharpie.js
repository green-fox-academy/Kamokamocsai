'use strict';

function Sharpie (color, width) {
    this.sharpieColor = color;
    this.sharpieWidth = width;
    this.inkAmount = 100;
    this.use = function() {
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