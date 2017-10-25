'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

for (var i = 0; i < girls.length; i++) {
    for (var j = 0; j < boys.length; j++) {
        if (i in order) {
            continue;
        } else if (j in order) {
            continue;
        } else {
            order.push(girls[i] + ' - ' + boys[j]);
        }
    }
}

console.log(order);