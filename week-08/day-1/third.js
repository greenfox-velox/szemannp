'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(width, height) {
  this.width = width;
  this.height = height;
};

Rectangle.prototype.getArea = function() {
  return this.width * this.height;
}

Rectangle.prototype.getCircumference = function() {
  return (this.width + this.height) * 2;
}

var myRect = new Rectangle(4, 5);

console.log(myRect.getArea());
console.log(myRect.getCircumference());

module.exports.Rectangle = Rectangle;
