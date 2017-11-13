'use strict';

let redditRequest = new XMLHttpRequest();
let mainSection = document.querySelector('section.posts');

let counter = 0;

function requestReddit (method, callback) {
    let url = 'http://secure-reddit.herokuapp.com/simple/posts'
    // let url = 'localhost:3000/posts'
    redditRequest.open(method, url, true);
    redditRequest.setRequestHeader('accept', 'application/json');
    redditRequest.onload = function(){
        let posts = JSON.parse(redditRequest.response);
        // console.log(posts)
        callback(posts);
    };
    redditRequest.send();
};

function listPosts(json){
    json.posts.forEach(function(element) {
        console.log(element.url);
        createHtml(element.url, element.title, calculateTime(element.timestamp), element.user);
    });
};

function createHtml (url, title, timestamp, user) {

    let post = document.createElement('div');
    post.classList.add('post');
    let username = user;
    if (username === null) {
        username = 'anonymous'
    };
    // post.createElement('a');
    
    post.innerHTML = `<div class="voter">
                        <img src="assets/upvote.png" id="upvote"/>
                        <span class="counter">`+ counter +`</span>
                        <img src="assets/downvote.png"/>
                     </div>
                     <div class="post-content">
                       <a href="` + url + `">` + title +`</a>
                       <p>submitted ` + timestamp + ` mins ago by ` + username + ` </p>
                       <a class="options" href="">Modify</a>
                       <a class="options" href="">Remove</a></div>`;

    mainSection.appendChild(post);
}

function calculateTime (timestamp) {
    let elapsedTime = Math.floor(timestamp/1000/60);
    return elapsedTime;
}

requestReddit('GET', listPosts);