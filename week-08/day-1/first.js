'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


// function letterObjectify(string) {
//   var letters = {};
//   var stringArray = string.split('');
//
//   stringArray.forEach(function(letter) {
//     if (!(letter in letters)) {
//       letters[letter] = 1;
//     } else {
//     letters[letter]++;
//     }
//   });
//   return letters;
// }

module.exports.letterObjectify = letterObjectify;

function letterObjectify(string) {
  return string.split('').reduce(function (string, letter) {
    string[letter] = (string[letter] + 1) || 1;
    return string;
  }, {});
}

console.log(letterObjectify('apple'));
