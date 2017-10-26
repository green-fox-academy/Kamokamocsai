'use strict';

let king = document.getElementById('b325');
console.log('king', king);

let conceited = document.getElementsByClassName('b326');
alert(conceited);

let businessLamp = document.getElementsByClassName('big');
console.log('businessLamp', businessLamp);

let conceitedKing = document.querySelectorAll('#b325, .b326');
alert('The King: ' + conceitedKing[0]);
alert('The conceited: ' + conceitedKing[1]);

let noBusiness = document.querySelectorAll('div');
console.log(noBusiness[0]);
console.log(noBusiness[1]);
console.log(noBusiness[2]);

let allBiznis = document.querySelector('p');
alert('AllBiznis: ' + allBiznis);