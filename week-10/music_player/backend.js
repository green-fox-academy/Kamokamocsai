'use strict';

const express = require('express');
const db = require('./assets/db.js');

let app = express();

app.use('/assets', express.static('./assets'));
app.use('/img', express.static('./img'));
app.use('/music', express.static('./music'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/music_player.html')
});

// app.get('/playlist-tracks', function(req, res) {
//     db.getAllTracks().then(data => res.json(data));
// });

// app.get('/playlist-tracks/:id', function(req, res) {
//     db.getTracksFromPlaylist(req.params.id).then(data => res.json(data));
// });

app.get('/playlists', function(req, res){
    let playlist = [
        { "id": 1, "title": "Favorites", "system": 1},
        { "id": 2, "title": "Music for programming", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ];
    res.json(playlist);
});

app.get('/trackinfo', function(request, response) {
    let trackList = [
        { "id": 1, "title": "birkát cserélek búzáért", "system": 1},
        { "id": 2, "title": "három az egyben váltok követ bármire", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0},
    ];
    response.json(trackList);
});

app.post('/trackinfo', function(request, response) {
    console.log(request.body);
    response.json({'status': 'done'});
});

app.listen(3000, () => console.log('Server is running...'));