'uses strict'

let headContent = document.querySelector('head');
alert(headContent.textContent);

let firstP = document.querySelector('p');
console.log(firstP.textContent);

let otherP = document.querySelector('.other');
alert(otherP.textContent);

headContent.innerHTML = '<title>New content</title>';

let resultP = document.querySelector('.result');
resultP.textContent = firstP.textContent;