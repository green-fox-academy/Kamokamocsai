'use strict';

const express = require('express');
// const mysql = require('mysql');
// const db = require('./assets/db.js');

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

// app.get('/playlists', function(req, res){
//     // res.json(playlist);
//     let responsePlaylists = [];
//     connection.query('SELECT * FROM playlist', function(err, rows){
//         if(err) {
//             console.log(err.toString());
//         };
//         console.log("Data received from Db:\n");
//         rows.forEach(function(element){responsePlaylists.push(element)
//     });
//     res.json(responsePlaylists);
//     });
// });

app.get('/playlists', function(req, res){
    res.json(playlist);
});

app.post('/playlists', function(req, res){
    playlist.push(req.body);
    res.json({"Status": "Done"});
});

app.post('/playlists', function(req, res){
    playlist.push(req.body);
    res.json({"Status": "Done"});
});

// let trackList = [
//     { "id": 1, "title": "birkát cserélek búzáért", "system": 1},
//     { "id": 2, "title": "három az egyben váltok követ bármire", "system": 0},
//     { "id": 3, "title": "Driving", "system": 0},
//     { "id": 4, "title": "Fox house", "system": 0},
// ];

// app.get('/trackinfo', function(request, response) {
//     response.json(trackList);
// });

// app.get("/trackinfo", function(request, response){
//     let data = [];
//     connect.query("Select * from Music;", function(err, results, fields){
//         results.forEach(function(element){data.push(element)
//         });
//         response.json(data);
//     });
//  });

// app.get('/trackinfo', function(req, res) {
//     let allSelector = 'SELECT * FROM music GROUP BY title';
//     conn.query(allSelector, function(err, rows){
//         if(err) {
//             console.log(err.toString());
//         }
//         console.log("Data received from Db:\n");
//         let responseAllTracks = {"tracklist": []};
//         rows.forEach(function(track){
//             responseAllTracks.tracklist.push({
//                 "id": track.id,
//                 "title": track.title,
//                 "artist": track.artist,
//                 "duration": track.duration,
//                 "path": track.path,
//                 "playlists": track.playlists_id
//             });
//         });
//         res.json(responseAllTracks);
//     });
// });

app.post('/trackinfo', function(request, response) {
    trackList.push(req.body);    
    response.json({'status': 'done'});
});

// let selector = function (){
    
// }

app.listen(3000, () => console.log('Server is running...'));