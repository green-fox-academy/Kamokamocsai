'use strict'


// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

let jail = function(name){
    this.fugitive = name;
    this.counter = 0;
    this.visit = function(){
        if (this.fugitive === ""){
            console.log("Nobody is here anymore");
        } else {
            this.counter++;
            console.log(this.fugitive + " is visited " + this.counter + " time(s)")
        }
    };
    this.escape = function(){
        console.log("BREAKING NEWS, " + this.fugitive + " escaped the prison");
        this.fugitive = "";
    }
}

let prison = function(name) {
    return new jail(name);
}

const alcatraz = prison('Sad Koala');

alcatraz.visit() // Sad Panda is visited 1 time(s)
alcatraz.visit() // Sad Panda is visited 2 time(s)
alcatraz.escape() // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit() // Nobody is here anymore