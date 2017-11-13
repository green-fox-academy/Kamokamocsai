'use strict';
const url = 'http://localhost:3000/API'

function ajax (command, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open(command, url);
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            callback(JSON.parse(xhr.responseText));
            console.log(JSON.parse(xhr.responseText));
        };
    };
    xhr.send();
};

let testFunc = function(item) {
    console.log(item);
};

let renderBook = (function(item){
    item.forEach(function(item) {
        let tempBook = document.createElement('p');
        tempBook.innerText = item.book_name;
        document.body.appendChild(tempBook);
    })
});

ajax('GET', renderBook);