'use strict';

let newPlaylistCreator = function () {
    var newListButton = document.querySelector('.new-playlist');
    var playlistForm = document.querySelector('.playlist-form');
    var createButton = document.querySelector('.create');
    var cancelButton = document.querySelector('.cancel');
    var input = document.querySelector('input');
    newListButton.addEventListener('click', function () {
        playlistForm.style.display = 'inline-block';
    });
    createButton.addEventListener('click', function () {
        var data = input.value;
        console.log(data);
        playlistForm.style.display = 'none';
        if(data != ""){
            let jsonData = {"id": 5, "title": data, "system": 0};
            console.log(jsonData);
            ajax('POST', jsonData, '/playlists', listPlayLists);
        };
        
    });
    cancelButton.addEventListener('click', function () {
        playlistForm.style.display = 'none';
    });
};

// let getPlaylists = function () {
//     ajax('GET', )
// };

newPlaylistCreator();