'use strict';

function Animal(name) {
    this.animalName = name;
    this.hungerProperty = 5;
    this.thirstProperty = 5;
    this.eat = function() {
        this.hungerProperty -= 1;
    }
    this.drink = function() {
        this.thirstProperty -= 1;
    }
    this.play = function() {
        this.hungerProperty += 1;
        this.thirstProperty += 1;
    }
}

function Farm(slots) {
    this.freePlaces = slots;
    console.log(this.freePlaces);
    this.listOfAnimals = [];
    this.breed = function(animal) {
        var animal = new Animal(animal);
        if (this.freePlaces > 0) {
            this.listOfAnimals.push(animal.animalName);
            this.freePlaces -= 1;
        } else {
            alert('No more free places!');
        }
    }
}

function getLittleFarm() {
    var littleFarm = new Farm(5);
}

function getMiddleFarm() {
    var middleFarm = new Farm(10);
}

function getBigFarm() {
    var bigFarm = new Farm(20);
}


let smallFarmButton = document.querySelector('.small');
smallFarmButton.addEventListener('click', getLittleFarm);

let middleFarmButton = document.querySelector('.middle');
middleFarmButton.addEventListener('click', getMiddleFarm);

let bigFarmButton = document.querySelector('.big');
bigFarmButton.addEventListener('click', getBigFarm);

smallFarmButton.addEventListener('click', disableButton);
middleFarmButton.addEventListener('click', disableButton);
bigFarmButton.addEventListener('click', disableButton);


function disableButton(){
    let smallButtAttr = smallFarmButton.setAttribute('disabled', 'true');
    console.log(smallButtAttr);
    if (smallFarmButton.getAttribute('disabled', 'true')){
        smallFarmButton.setAttribute('disabled', 'false');
    }else{
        smallFarmButton.setAttribute('disabled', 'true');
    }
}

console.log(smallFarmButton.getAttribute('disabled'));

let breedGoat = document.querySelector('.goat');
// breedGoat.addEventListener('click', getLittleFarm.breed('goat'));
// console.log(getLittleFarm.bind);

// littleFarm.breed('goat');

// kecskeFarm.breed('kecske');
// kecskeFarm.breed('juhocska');
// kecskeFarm.breed('t-rexecske');



console.log(Farm.listOfAnimals);