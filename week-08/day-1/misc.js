'use strict';

var add = require('./add');
var tape = require('');

tape(function(t) {
  t.equal(add(1, 2), 3);
  t.end();
});
