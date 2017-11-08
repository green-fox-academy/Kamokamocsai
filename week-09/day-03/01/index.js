let express = require('express');
let app = express();

// let counter = 0;

express.json.type = "application/json";
app.use('/assets', express.static('./assets')); // az assets helyett stuff lesz az elérésnél

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(request, response){
    if(request.query.input === undefined){
        response.json({
            'error': "Please provide an input!"
        })
    }else if (request.query.input == ""){
        console.log('Pls provide an input!');
        response.json({
            "error": "Please provide an input!"
        })
    } else {
        response.json({
            'received': request.query.input,
            'result': request.query.input * 2
        });
    }
});

app.get('/greeter', function(request, response){

    if(request.query.name === undefined){
        response.json({
            "error": "Please provide a name!"
        })
    } else if (request.query.title === undefined) {
        response.json({
            "error": "Please provide a title!"
        })
    } else {
        response.json({
            "welcome_message": "Oh, hi there " + request.query.name + ", my dear " + request.query.title + "!"
        });
    };
});

app.get('/appenda/:appendable', function(request, response){
    response.json({
        'appended': request.params.appendable + 'a'
    })
});

app.use(express.json());

app.post('/dountil/:what', function(request, response){
    
})

// app.get('/hello', function(request, response){
//     counter++;
//     response.json({hello: counter});
// });

app.listen(3000, () => console.log('LocalServer (localhost:3000) is running...'));
