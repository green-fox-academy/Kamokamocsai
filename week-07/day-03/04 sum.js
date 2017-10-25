'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum (input) {
    let sumNumbers = 0;
    for (var i = 0; i <= input; i++) {
        sumNumbers += i;
    }
    return sumNumbers;
}

console.log(sum(10))