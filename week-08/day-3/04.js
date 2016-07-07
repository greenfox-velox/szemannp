'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

var fs = require('fs');

function concatTextFiles(textFile1, textFile2, cb) {
  fs.readFile(textFile1, 'utf8', function(err, textContent) {
    if (err) {
      cb(err);
    }
    var concatContent = textContent.trim();
    fs.readFile(textFile2, 'utf8', function(err, textContent) {
      concatContent += textContent.trim();
      if (err) {
        cb(err);
      }
      cb(null, concatContent);
    });
  });
}

concatTextFiles('text_1.txt', 'text_2.txt', function(err, concatContent) {
  console.log(err, concatContent);
});
