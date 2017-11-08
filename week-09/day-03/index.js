let express = require('express');
let app = express();

let counter = 0;

app.use('/stuff', express.static('./assets')); // az assets helyett stuff lesz az elérésnél

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
});

app.get('/hello', function(request, response){
    counter++;
    response.json({hello: counter});
});

app.listen(3000, () => console.log('App is running...'));
