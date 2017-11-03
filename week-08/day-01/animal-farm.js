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
    let breedGoat = document.querySelector('.goat');
    breedGoat.addEventListener('click', breedAnimal('goat'));
    this.breed = function(animal) {
        var animal = new Animal(animal);
        if (this.freePlaces > 0) {
            this.listOfAnimals.push(animal.animalName);
            this.freePlaces -= 1;
            getListOfAnimals(this.listOfAnimals);
        } else {
            alert('No more free places!');
        }
    }

    function breedAnimal (animal) {
        var animal = new Animal(animal);
        if (this.freePlaces > 0) {
            this.listOfAnimals.push(animal.animalName);
            this.freePlaces -= 1;
            getListOfAnimals(this.listOfAnimals);
        } else {
        alert('No more free places!');
        }
    }
}

function getLittleFarm() {
    var littleFarm = new Farm(5);
    // let breedGoat = document.querySelector('.goat');
    // breedGoat.addEventListener('click', littleFarm.breed('goat'));
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
    smallFarmButton.setAttribute('disabled', 'true');
    middleFarmButton.setAttribute('disabled', 'true');
    bigFarmButton.setAttribute('disabled', 'true');
}

// console.log(getLittleFarm.bind);

// littleFarm.breed('goat');

// kecskeFarm.breed('kecske');
// kecskeFarm.breed('juhocska');
// kecskeFarm.breed('t-rexecske');



console.log(Farm.listOfAnimals);

function getListOfAnimals(listOfAnimals){
    let animalsList = document.querySelector('.list');
    animalsList.textContent = listOfAnimals;
}


function getStatus(){

}