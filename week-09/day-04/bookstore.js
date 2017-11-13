'use strict';

const express = require('express');
const app = express();
const mysql = require('mysql');

app.use('/assets', express.static('./assets'));
express.json.type = "application/json";
app.use(express.json());

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'bookstore'
});

conn.connect(function(err){
    if(err){
        console.log("Error connecting to Db");
        return;
    } else {
        console.log("Connection established");
    }
});

app.get('/', function(req,res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/list', function(req, res){
    conn.query('SELECT book_name FROM book_mast;', function(err, rows){
        if(err) {
            console.log(err.toString());
        }
        console.log("Data received from Db:\n");
        let htmlString = '<ul>';
        rows.forEach(function(row) {
            htmlString = htmlString + '<li>' + row.book_name + '</li>';
        });
        htmlString = htmlString + '</ul>';
        res.send(htmlString)
    });
});

app.listen(3000, () => console.log('Bookstore Server is listening in 3000'));