'use strict';

let dataFromPlaylists = document.querySelector('.playlist');
let playTrack = document.querySelector('.playlist');

let listPlayLists = function(){
    dataFromPlaylists.innerHTML = null;
    ajax('GET', '', '/playlists', playListData);
};

let playListData = (data) => {
    console.log(data);
    data.forEach(function(e) {
        let play = document.createElement('li');
        dataFromPlaylists.appendChild(play);
        play.textContent = e.title;
    });
    highLight();
};

let highLight = () => {
    let liElements = dataFromPlaylists.querySelectorAll('li');
    liElements.forEach(function(e){
        e.addEventListener('click', function() {
            liElements.forEach(e => e.classList.remove('active'));
            e.classList.add('active');
        });
    });
};

let listTrackLists = function(){
    playTrack.innerHTML = null;
    ajax('GET', '', '/playlists', trackListData);
};

let trackListData = (data) => {
    console.log(data);
    data.forEach(function(e) {
        let play = document.createElement('li');
        playTrack.appendChild(play);
        play.textContent = e.title;
    });
    highLight();
};