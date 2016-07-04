'use strict';


var numbers = [12, 25, 3, 44, 5];

var sum = numbers.reduce(function(acc, e, i, arr) {
  return acc + e;
});


var evens = numbers.reduce(function(acc, e) {
  if (e % 2 === 0) {
    acc.push(e);
  }
  return acc;
}, []);
