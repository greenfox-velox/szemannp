'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function summarizer(array) {
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum;
}

console.log(summarizer(numbers));
