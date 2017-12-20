'use strict'

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use(express.json());

app.use(express.static(__dirname + '/assets'));

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'licence_plate'
});

connection.connect(function (err){
    if(err){
        console.log('Error connecting to DB!');
        return;
    };
    console.log('Connected to the Database.');
});

app.get('/', function (req, res){
    res.sendFile(__dirname + '/assets/index.html');
});

app.get('/search', function(req, res){
    let filter = '';
    
    if( req.query.police ){  // query stringben átjövő adat
        filter = 'RB%';
    };
    
    if( req.query.diplomat ){
        filter = 'DT%';
    };
    let sqlCode = `SELECT * FROM licence_plates WHERE plate LIKE "${filter}%${req.query.plate}%"`; // A ? jel helyére jön a [] közötti req.query.plate!!!
    
    connection.query(sqlCode, function(err, rows){
        res.send({
            "result": "ok",
            "data": rows
        });
    });
});

app.get('/search/:brand', function (req, res) {
    let sqlCode = `SELECT * FROM licence_plates WHERE car_brand="${req.params.brand}"`;
    connection.query(sqlCode, function (err, row){
        res.send({
            "result": "ok",
            "data": row
        });
    });
});

app.get('/add', function (req, res) {
    // console.log(req.query.plate);
    let sqlCode = `INSERT INTO licence_plates (plate, car_brand, car_model, color, year) VALUES ("${req.query.plate}", "${req.query.brand}", "${req.query.model}", "${req.query.color}", "${req.query.year}")`;
    connection.query(sqlCode, function (err, row){
        res.send({
            "result": "ok",
            "data": row
        });
    });
});



app.listen(3000, () => console.log('Server is running...'));