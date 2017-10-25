'use strict';

var example = "In a dishwasher far far away";

// I would like to replace "dishwasher" with "galaxy" in this example
// Please fix it for me!
// Expected ouput: In a galaxy far far away

function replacer(example) {
    var splittedWords = example.split(' ');
    splittedWords[2] = 'galaxy';
    example = splittedWords.join(' ');
    return example;
}

example = replacer(example);

console.log(example);