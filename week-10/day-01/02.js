'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

const Rectangle = function(parameters1, parameters2) {
    this.parameters1 = parameters1
    this.parameters2 = parameters2
}

Rectangle.prototype.getArea = function() {
    return this.parameters1 * this.parameters2
}

Rectangle.prototype.getCircumference = function() {
    return this.parameters1 * 2 + this.parameters2 * 2
}

const rectOne = new Rectangle(5,10)
console.log(rectOne.getArea(), rectOne.getCircumference())