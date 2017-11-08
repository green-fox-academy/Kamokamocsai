'use strict';

let test = require('tape');
let summer = require('./02sum.js');

test('something ', function(t){
    let list1 = [1, 2, 3];
    let summing = new summer();
    t.equal(summing.sumNumbers(list1), 6);
    t.end();
});
