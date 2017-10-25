'use strict';
// Add "a" to every string in far

var far = ["kuty", "macsk", "kacs", "rók", "halacsk"];
var tempOut = [];

for (var i = 0; i < far.length; i++) {
    tempOut.push(far[i]+'a');
}

far = tempOut;
console.log(far);