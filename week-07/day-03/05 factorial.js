'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio (input) {
    var numberFactorial = 1;
    for (var i = 1; i <= input; i++){
        numberFactorial *= i;
    }
    return numberFactorial;
}

console.log(factorio(10));