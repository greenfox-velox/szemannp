'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function evenSelector(array) {
    var evens = [];
    for (var i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            evens.push(array[i]);
        }
    }
    return evens;
}

console.log(evenSelector(numbers));
