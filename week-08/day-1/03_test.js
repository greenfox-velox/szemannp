'use strict';

var rect = require('./third');
var tape = require('tape');

tape(function(t) {
  var rectTest = new rect.Rectangle(3, 5);
  t.deepEqual(rectTest.getArea(), 15);
  t.deepEqual(rectTest.getCircumference(), 16);
  t.end();
});
