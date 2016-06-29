'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}


var myString = 'majomkenyer';

function letterCounter(string) {
    var letterArray = string.split('');
    var letters = {};
    letterArray.forEach(function(item) {
        if (!(item in letters)) {
            letters[item] = 1;
        } else {
            letters[item]++
        }
    });
    return letters;
}
console.log(letterCounter(myString));
