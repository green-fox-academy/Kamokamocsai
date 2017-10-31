'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

console.log('apple');
setTimeout(() => console.log('pear'), 1000);
setTimeout(console.log, 3000, 'melon');
setTimeout(console.log, 5000, 'grapes');

