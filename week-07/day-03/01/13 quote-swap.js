'use strict';
// Accidentally I messed up this quote from Richard Feynman.
// Two words are out of place
// Your task is to fix it by swapping the right words with code

// Also, log the sentence to the console with spaces in between. cannot and do

var words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."];

var index1 = words.indexOf('do');
var index2 = words.indexOf('cannot');

[words[index1], words[index2]] = [words[index2], words[index1]];

console.log(words.join(' '));