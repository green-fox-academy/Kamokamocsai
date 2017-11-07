'use strict';

let test = require('tape');
let add = require('./01apple.js');

test('returns apple', function (t) {
    t.equal(add.getApple(), 'apple');
    t.end();
});