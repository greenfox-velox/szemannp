'use strict';

// create a function that returns it's input factorial

function factorial(number) {
    var fact = 1;
    for (var i = 1; i < number; i++) {
        fact *= i;
    }
    return fact;
}

console.log(factorial(5));
