'use strict';


let ajax = function(method, data, response, callback) {
    let foxPlayer = new XMLHttpRequest();
    data = data ? data : null;
    foxPlayer.open(method, 'http://localhost:3000' + response);
    foxPlayer.setRequestHeader('Content-Type', 'application/json');
    foxPlayer.send(JSON.stringify(data));
    foxPlayer.onreadystatechange = function() {
        if (foxPlayer.readyState === XMLHttpRequest.DONE) {
            callback( JSON.parse(foxPlayer.response))
        };
    };
};