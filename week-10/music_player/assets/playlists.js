'use strict';

let playTrack = document.querySelector('.playlist');

let listPlayLists = function(){
    ajax('GET', '', '/playlists', playListData);
};

let playListData = (data) => {
    console.log(data);
    data.forEach(function(e) {
        let play = document.createElement('li');
        playTrack.appendChild(play);
        play.textContent = e.title;
    });
    highLight();
};

let highLight = () => {
    let liElements = playTrack.querySelectorAll('li');
    liElements.forEach(function(e){
        e.addEventListener('click', function() {
            liElements.forEach(e => e.classList.remove('active'));
            e.classList.add('active');
        });
    });
};

// let create = () => {
//     let addPlayList = document.querySelector('.add');
//     let body = document.querySelector('body');
//     addPlayList.addEventListener('click' , function() {
//         let inputElement = document.createElement('input');
//         inputElement.classList.add('user-input');
//         body.appendChild(inputElement);
//     });
// };

let postList = function() {
    ajax('POST', {'szia': 'hali'}, '/trackinfo', console.log);
};

// create();