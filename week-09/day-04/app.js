var mysql = require("mysql");

var conn = mysql.createConnection({
  host: "localhost",
  user: "jaj",
  password: "alma"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

conn.end();