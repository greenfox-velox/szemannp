'use script';

var countBooks = require('./second');
var tape = require('tape');

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var students2 = [
  {name: 'Mike', age: 12},
  {name: 'Bob', age: 11},
  {name: 'Shela', age: 14},
  {name: 'Charles', age: 9},
  {name: 'Jess', age: 12},
  {name: 'Bob', age: 15}
];

tape(function(t) {
  t.deepEqual(countBooks.countBooks(students), 4);
  t.end();
});

tape(function(t) {
  t.deepEqual(countBooks.countBooks(students2), 0);
  t.end();
});
