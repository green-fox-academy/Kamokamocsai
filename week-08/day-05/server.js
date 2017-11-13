let express = require('express');
let app = express();


let counter = 0;
let idnum = 0;

app.use('/assets', express.static('./assets'));

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html');
});

// app.get('/posts', function(request, response){
//     idnum++;
//     counter++;
//     response.json({'posts':[{
//         'id': idnum, 'title': title, 'url': url, 'timestamp': timestamp, 'score': counter, 'user': user
//     }]});
// });

app.listen(3000, () => console.log('The Server is running...'));