'use strict';

var button = document.getElementById('submit')

button.addEventListener('click', click);

function getData (place, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=' + place);
    xhr.setRequestHeader('X-Mashape-Key', )
    xhr.onreadystatechange = function () {
        if(xhr.readyState === 4) {
            let data = JSON.parse(xhr.responseText);
            callback(data);
        }
    xhr.send();
    console.log('Request sent');
    }
    function handleData(parsedData){
        if(parsedData.Results.length > 0) {
            console.log(parsedData.Results[0]);
            lat.innerText += " " + parsedData.Results[0].lat;
            long.innerText += " " + parsedData.Results[0].lon;
        }else {
            console.log('No');
            document.getElementById('warn').innerText = "No location found";
        }
    }
    function click(){
        console.log('click event');
        var location = document.getElementById('location');
        if (location !== ''){
            getData(location, handleData);
        }
    }
}


getData('Budapest', test);