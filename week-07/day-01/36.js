'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah

var sum = 0;
var counter = 0;

while (counter < ah.length) {
    sum += ah[counter];
    counter++;
}
console.log(sum)
