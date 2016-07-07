'use strict';


var fs = require('fs');

var files = ['text_1.txt', 'text_2.txt', 'text_3.txt'];
var resultContainer = [null, null, null];

function readFirstFile(fileName, cbFunction) {
  fs.readFile(fileName, 'utf8', function(err, firstContent) {
    if (err) {
      cb(err);
    }
    resultContainer[0] = firstContent.trim();
  });
}

function readSecondFile(fileName, cbFunction) {
  fs.readFile(fileName, 'utf8', function(err, secondContent) {
    if (err) {
      cb(err);
    }
    resultContainer[1] = secondContent.trim();
  });
}

function readThirdFile(fileName, cbFunction) {
  fs.readFile(fileName, 'utf8', function(err, thirdContent) {
    if (err) {
      cb(err);
    }
    resultContainer[2] = thirdContent.trim();
  });
}

var timer = setInterval(checkResult(), 50);

function checkResult() {
  for (var i = 0; i < files.length; i++) {
    var counter = 0;
    if (files[i].isString) {
      counter++;
      if (counter === 3) {
        clearInterval(timer);
        console.log(files[0] + files[1] + files[2]);
      }
    }
  }
}


function getResult(arrayName, cbFunction) {
  readFirstFile(arrayName[0]);
  readSecondFile(arrayName[1]);
  readThirdFile(arrayName[2]);
  setInterval(checkResult(), 50);

}

getResult(files, function() {
  checkResult();
});
