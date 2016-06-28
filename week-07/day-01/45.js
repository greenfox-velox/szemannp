'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function longestStringFinder(array) {
    var shortest = array[0];
    for (var i = 0; i < array.length; i++) {
        if (array[i].length < shortest.length) {
            shortest = array[i];
        }
    }
    return shortest;
}

console.log(longestStringFinder(names));
