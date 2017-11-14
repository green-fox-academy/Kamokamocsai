'use strict';

let express = require('express');
let mysql = require('mysql');
let app = express();

let connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'a',
    database: 'bookstore'
});

connection.connect();

function getDatabase(tableName, what, callback){
    let searchQuery = 'SELECT ' + what + ' FROM ' + tableName;
    connection.query(searchQuery, function(error, results, fields){
        console.log(results);
        callback(results, what);
    });
};

function handleSqlData(sqlResults){
    let returnData = [];
    sqlResults.forEach(function(element) {
        console.log(element[fieldName]);
        returnData.push(element[fieldName]);
    });
    console.log(sqlResults);
}

app.get('/books', function(req, res){
    getDatabase('book_mast', 'book_name', handleSqlData);
    res.send('hello');
});


app.listen(3000, () => console.log('Server is running...'));