'use strict';
// Create a simple calculator application which does read the parameters from the standard input 
// and prints the result to the console.

// It should support the following operations: 
// +, -, *, /, % and it should support two operands. 

// The format of the expressions must be: {operation} {operand} {operand}. 
// Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

// You should use the command line arguments to accept user input

// It should work like this:

// Start the program with "node calculator.js + 5 6"
// If number of arguments are not correct, print some nice errors
// Else print the result
// Say goodbye

var args = process.argv.splice(2); // Just a helper for you to get started

var solution = 0;

function calculator(args) {
    if (args == '') {
        return 'Error: No Valid Parameters!'
    } else if (args[0] === '+') {
        solution = Number(args[1]) + Number(args[2]);
        return solution;
    } else if (args[0] === '-') {
        solution = Number(args[1]) - Number(args[2]);
        return solution;
    } else if (args[0] === '*') {
        solution = Number(args[1]) * Number(args[2]);
        return solution;
    } else if (args[0] === '/') {
        solution = Number(args[1]) / Number(args[2]);
        return solution;
    } else {
        return 'Wrong parameters! The correct syntax is: {operation} {operand} {operand}';
    }
}

console.log('The result is: ' + calculator(args));
console.log('Input params are', args);
console.log('Goodbye!');