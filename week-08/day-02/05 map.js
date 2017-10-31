'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.


function letterSummer(word){
    var allLetters = word.split('');
    var eCounterNumber = 0;
    allLetters.forEach(function(element) {
        if (element === 'e'){
            eCounterNumber += 1;
        }
    })
    return eCounterNumber;
}

var letterE = fruits.map(letterSummer);

console.log(letterE);