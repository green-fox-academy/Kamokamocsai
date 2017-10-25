'use strict';
// When saving this quote a disk error has occured. Please fix it.
// Add "always takes longer than" to between the words "It" and "you"

var quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

quote = quote.split('It you').join('It always takes longer than you');

// quote = quote.slice(0, quote.indexOf("you")) + "always takes longer than" + quote.slice(quote.indexOf("you")-1);

console.log(quote);