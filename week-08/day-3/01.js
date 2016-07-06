'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

// var fs = require('fs');
//
// var cbShowResult = function(result) {
//   console.log(result);
// }
//
// var cbGetContent = function(fileName, cbFunction) {
//   data = fs.readFile(fileName, getWordsAmount(data, cbShowResult));
// };
//
// var getWordsAmount = function(data, cbFunction) {
//   String(data).split(/\s/g).length;
// };
//
// var wordCount = function(data) {
//
// }
//
//
// wordCount('majom.txt', cbGetContent);



function wordCount(fileName, cb) {
  fs.readFile(fileName, function(err, content) {
    if (err) {
      return cb(err);
    }
    var count = String(content).split(/\s/g).length;
    cb(null, count);
  });
}

wordCount('zsomle.txt', function(err, c) {
  console.log(err, c);
});
