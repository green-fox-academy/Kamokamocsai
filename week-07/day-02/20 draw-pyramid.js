'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

let whiteSpace = ' ';
let spaceCounter = lineCount - 1;

for (let i = 1; i <= lineCount; i++) {
    console.log(whiteSpace.repeat(spaceCounter) + "*".repeat(i * 2 - 1));
    spaceCounter -= 1;
}