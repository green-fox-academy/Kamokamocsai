'use strict';

let postTitle = document.getElementById('title');
let postUrl = document.getElementById('url');
let submitButton = document.querySelector('a.sendpost');

const postData = {
    "title": "",
    "url": ""
};

function post(data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts');
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onload = function() {
        window.location.href = '/'     //redirects back to main page
    };
    xhr.send(JSON.stringify(data));   //string need to be sent to server, so first the objects shoulb be converted into string
};

submitButton.addEventListener('click', function() {
    postData.title = document.querySelector('input.title').value;
    postData.url = document.querySelector('input.url').value;
    console.log(postData);
    if ( postData.title !== '') {
        post(postData);
    } else {
        alert('Title field is empty! Please write something in it.');
    };
});