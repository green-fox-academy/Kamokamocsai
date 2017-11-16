'use strict';

const express = require('express');
const mysql = require('mysql');
const db = require('./assets/db.js');

let app = express();

app.use('/assets', express.static('./assets'));
app.use('/img', express.static('./img'));
app.use('/music', express.static('./music'));
app.use(express.json());

app.get('/', function(req, res){
    res.sendFile(__dirname + '/music_player.html')
});

// app.get('/playlist-tracks', function(req, res) {
//     db.getAllTracks().then(data => res.json(data));
// });

// app.get('/playlist-tracks/:id', function(req, res) {
//     db.getTracksFromPlaylist(req.params.id).then(data => res.json(data));
// });

let playlist = [
    { "id": 1, "title": "Favorites", "system": 1},
    { "id": 2, "title": "Music for programming", "system": 0},
    { "id": 3, "title": "Driving", "system": 0},
    { "id": 4, "title": "Fox house", "system": 0},
];

app.get('/playlists', function(req, res){
    res.json(playlist);
});

app.post('/playlists', function(req, res){
    playlist.push(req.body);
    res.json({"Status": "Done"});
});

let trackList = [
    { "id": 1, "title": "birkát cserélek búzáért", "system": 1},
    { "id": 2, "title": "három az egyben váltok követ bármire", "system": 0},
    { "id": 3, "title": "Driving", "system": 0},
    { "id": 4, "title": "Fox house", "system": 0},
];

app.get('/trackinfo', function(request, response) {
    response.json(trackList);
});

app.post('/trackinfo', function(request, response) {
    trackList.push(req.body);    
    response.json({'status': 'done'});
});

// let selector = function (){
    
// }

app.listen(3000, () => console.log('Server is running...'));