'use strict';
// Saturn is missing from the planetList
// Insert it into the correct position
// bonus for using some built in methods

var planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"];

var halfOfList = planetList.splice(5, 7);
planetList.push('Saturn,');
planetList += halfOfList;
console.log(planetList);