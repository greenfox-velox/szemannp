'use strict';

// print the even numbers till 20

var counter = 0;

while (counter <= 20) {
    if ((counter + 2) % 2 === 0) {
        console.log(counter)
    }
    counter++
}
