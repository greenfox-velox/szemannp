'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var myString = 'abrakadabra'

function isLetterMatching(string, letter) {
    return string.split('').some(function(e) {
        return (e === letter);
    });
}

console.log(isLetterMatching(myString, 'r'));


function isLetterMatchingShortHanded(string, letter) {
    return string.indexOf(letter) != -1;
}

console.log(isLetterMatchingShortHanded(myString, 'r'));
