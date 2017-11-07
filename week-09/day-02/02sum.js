// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
// Follow these steps:
// Add a new test case
// Instantiate your class
// create a list of integers
// use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
// test your method with an empyt list
// with a list with one element in it
// with multiple elements in it
// with a null
// with a string
// Run them
// Fix your code if needed

'use strict';

class Sum {
    sumNumbers (list) {
        if (list.length === 0) {
            list = [0];
        }
        let summa = list.reduce(function(sum, value){
            return sum + value;
            })
    return summa;
        }
};

module.exports = Sum;