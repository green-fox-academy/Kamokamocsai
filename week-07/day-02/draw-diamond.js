'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

let whiteSpace = ' ';
let spaceCounter = lineCount - 1;
let middleNumber = Math.round(lineCount/2);
let afterSpace = 0;

for (let i = 1; i <= lineCount; i++) {
    if (i < middleNumber) {
        console.log(whiteSpace.repeat(spaceCounter) + "*".repeat(i * 2 - 1));
        spaceCounter -= 1;
    } else if (i == middleNumber) {
        console.log(whiteSpace.repeat(spaceCounter) + "*".repeat(i * 2 - 1));
        spaceCounter +=1;
    } else if(i > middleNumber) {
        console.log(whiteSpace.repeat(spaceCounter) + "*".repeat(i - afterSpace));
        afterSpace += 1;
        spaceCounter += 1;        
    }

}