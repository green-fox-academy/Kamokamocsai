'use strict';

const mysql = require('mysql');

const connection = mysql.createConnection({
    user: 'root',
    password: 'gameskami',
    database: 'music',
    host: 'localhost'
});

connection.connect(function(err) {
    if (err) {
        console.log(err);
        return;
    }
    console.log('MYSQL connection established');
});

// const mysqlPromise = function(query) {
//     return new Promise(function (resolve, reject) {
//         connection.query(query, function(err, results) {
//             if (err) {
//                  reject(err);
//             } else{
//                 resolve(results);
//             };
//         });
//     });
// };

// const getAllPlaylists = function() {
//     return mysqlPromise(`
//         SELECT * FROM playlists;    
//     `);
// };

// const getAllTracks = function() {
//     return mysqlPromise(`
//         SELECT * FROM tracks;    
//     `);
// };

// const getTracksFromPlaylist = function(id) {
//     return mysqlPromise(`
//         SELECT * FROM tracks 
//         JOIN playlistTracks ON tracks.id = playlistTracks.trackID
//         WHERE playlistID = ${mysql.escape(id)} AND 
//         tracks.id = playlistTracks.trackID;
//     `);
// };

// module.exports = {
//     getAllPlaylists,
//     getAllTracks,
//     getTracksFromPlaylist
// };