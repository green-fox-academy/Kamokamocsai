'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]

var index1 = listOfNumbers.indexOf(2);
var index2 = listOfNumbers.indexOf(8);
var index3 = listOfNumbers.indexOf(14);
var index4 = listOfNumbers.indexOf(16);

function numChecker(listOfNumbers) {
    if (index1 !== -1 && index2 !== -1 && index3 !== -1 && index4 !== -1) {
        return true;
    } else {
        return false;
    }
}

console.log(numChecker(listOfNumbers));