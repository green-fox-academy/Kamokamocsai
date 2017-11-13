'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

const Animals = function(word){
    this.word = word;
};

let cat = new Animals('Meow');

Animals.prototype.say = function (){
    console.log(this.word);
}

cat.say();