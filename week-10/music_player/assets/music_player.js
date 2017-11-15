const controller = function () {
    this.init = function () {
        this.newPlaylistCreator()
    };
    this.newPlaylistCreator = function () {
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
            playlistForm.style.display = 'none';
            // postNewPlaylist(displayPlaylists, data)
        });
        cancelButton.addEventListener('click', function () {
            playlistForm.style.display = 'none';
        });
    };
};

const cont = new controller;
cont.init();