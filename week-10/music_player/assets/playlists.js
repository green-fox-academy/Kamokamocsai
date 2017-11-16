'use strict';

let playTrack = document.querySelector('.playlist');

let listPlayLists = function(){
    playTrack.innerHTML = null;
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

// let postNewPlaylist = function() {
//     ajax('POST', data, '/playlists', playListData);
// };