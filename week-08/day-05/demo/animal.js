class Animal {    
    constructor() {
        this.hunger = 5; 
        this.thirst = 5; 
    };

    eat() {
        this.hunger--;
    };

    drink() {
        this.thirst--;
    };

    play() {
        this.hunger++;
        this.thirst++;
    };
}

class Farm { 
    constructor(amount, type) {
        this.freeSlots = amount;
        this.animals = [];
};

    breed() {
        if (this.freeSlots > this.animals.length) {
            this.animals.push(new Animal());
        } else {
            console.log("The farm is full.");
        }
    };

    slaughter() {
        if (this.animals.length === 0) {
            return "We have no animals to slaughter."
        } else {
            let wellFedIndex = 0;
            let minHunger = 5;
            this.animals.forEach(function(element, i) {
                if (element.hunger <= minHunger) {
                    minHunger = element.hunger;
                    wellFedIndex = i;
                }
            });
            this.animals.splice(wellFedIndex, 1);
        };
    };

    getRandom() {
        return Math.round(Math.random());
    };

    progress() {
        this.animals.forEach(function(element) {
            let activities = ["eat", "drink", "play"]
            activities.forEach(function(each) {
                let random = this.getRandom();
                if (random === 1) {
                    element[each]();
                };
            }.bind(this));
        }.bind(this));
    };

    status() {
        if (this.freeSlots === animals.length) {
            return 
        }
        console.log("The farm has " + this.animals.length + " living animals. We are bankrupt.");
    }
};

const SheepFarm = new Farm(20)

let result = document.querySelector("#result");


let refresh = function(){
number.textContent = SheepFarm.animals.length;
result.textContent = getResult();
};


let getResult = function() {
if (SheepFarm.animals.length === 0) {
    return "bankrupt";
} else if (SheepFarm.animals.length === SheepFarm.freeSlots) {
    return "full";
} else {
    return "okay";
};
};


let breeding = document.querySelector("#breed");
breeding.addEventListener("click", function() {
    SheepFarm.breed();
    refresh();
    console.log("breeding");
});

let number = document.querySelector("#animals");
number.textContent = SheepFarm.animals.length;
let size = document.querySelector("#size");
size.textContent = SheepFarm.freeSlots;
let progressing = document.querySelector("#prog");
let showProgress = document.querySelector("#show_progress");

progressing.addEventListener("click", function() {
    SheepFarm.progress()
    showProgress.textContent = SheepFarm.animals.forEach(function(element) {
        return "Animal hunger: " + element.hunger + ", Animal thirst: " + element.thirst;
    });
});

let kill = document.querySelector("#kill");

kill.addEventListener("click", function() {
    showProgress.textContent = SheepFarm.slaughter();
    refresh();
});

let endOfDay = document.querySelector("#day");

endOfDay.addEventListener("click", function() {
    SheepFarm.breed();
    SheepFarm.slaughter();
    showProgress.textContent = "A day has passed, and one sheep has born, and one has been slaughtered for the blood gods!"
});

SheepFarm.animals;

SheepFarm.status();

console.log(SheepFarm.animals);