'use strict';

var ah = ['kuty', 'macsk', 'cic']
// add to all elements an 'a' on the end

var counter = 0;

while (counter < ah.length) {
    ah[counter] += 'a';
    counter++;
}

console.log(ah)
