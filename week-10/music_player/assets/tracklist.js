'use strict';


let trackList = document.querySelector('.tracklist');

let trackInfo = function(){
    ajax('GET', '', '/trackinfo', trackInfoData);
};

let trackInfoData = (data) => {
    data.forEach(function(e) {
        let track = document.createElement('li');
        trackList.appendChild(track);
        track.textContent = e.id;
        track.textContent += ". " + e.title;
    });
};