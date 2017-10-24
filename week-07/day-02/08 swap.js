'use strict';

// Swap the values of these variables
var a = 123;
var b = 526;

// b = [a, a = b][0];

[a, b] = [b, a]

console.log(a);
console.log(b);