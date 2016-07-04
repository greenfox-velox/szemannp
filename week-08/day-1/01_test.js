'use strict';

var letterObjectify = require('./first');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(letterObjectify.letterObjectify('zzz'), {z: 3});
  t.end();
});
