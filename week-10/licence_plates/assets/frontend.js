'use strict'

const localhost = 'http://localhost:3000';
const queryButton = document.querySelector('#search');
const searchInput = document.querySelector('#searchField');
const searchInputByBrand = document.querySelector('#searchFieldByBrand');
let solutionField = document.querySelector('.solution');
const resetButton = document.querySelector('#reset');
const police = document.querySelector('#police');
const diplomat = document.querySelector('#diplomat');
const allInputFields = document.querySelectorAll('.inputfield');

resetButton.addEventListener('click', function(){
    let allRadioButtons = document.querySelectorAll('.radiobtn');
    allRadioButtons.forEach((function(radioButton){
        if (radioButton.checked){
            radioButton.checked = false;
        };
    }));
    solutionField.innerHTML = "";
});

queryButton.addEventListener('click', startSearch);

allInputFields.forEach (function (elements){
    elements.addEventListener('keypress', function(e){
        var key = e.which || e.keyCode;
        if (key === 13) { // 13 is enter
            startSearch();
        };
    });
});

function startSearch () {
    console.log('click event');
    console.log(searchInputByBrand.value)
    let searchValue = searchInput.value;
    let inputBrand = searchInputByBrand.value;
    let filter = false;
    
    if ( inputBrand !== "") {
        let brandUrl = localhost + "/search/" + inputBrand;
        console.log(brandUrl)
        ajax('GET', brandUrl, createTable);
    } else {
        if ( police.checked ) {
            filter = 'police';
        };
        
        if ( diplomat.checked ) {
            filter = 'diplomat';
        };
        
        let url = getSearchURL(searchValue, filter);
        ajax('GET', url, createTable);

    };    
};

function getSearchURL(plateNum, filter){
    let apiEndpoint = localhost + '/search?plate=';
    apiEndpoint += plateNum;
    
    if (filter){
        apiEndpoint += '&' + filter + '=1';
    };
    return apiEndpoint;
};

function ajax (method, url, callback) {
    let xhr = new XMLHttpRequest;
    xhr.open(method, url);
    solutionField.innerHTML = "";    
    solutionField.innerHTML += `<center><h1>Please wait for the data!`;
    xhr.onload = function () {
        callback( JSON.parse(xhr.responseText) );
    };
    xhr.send();
};

function createTable (response) {
    solutionField.innerHTML = "";
    let table = document.createElement('table');
    solutionField.appendChild(table);
    table.innerHTML += `<tr>
                            <th>Plate</th>
                            <th>Brand</th>
                            <th>Model</th>
                            <th>Color</th>
                            <th>Year</th>
                        </tr>`

    response.data.forEach(function(car){
        table.innerHTML += `<tr>
                                <td>${car.plate}</td>
                                <td><a id="${car.car_brand}">${car.car_brand}</a></td>
                                <td>${car.car_model}</td>
                                <td>${car.color}</td>
                                <td>${car.year}</td>
                                <td style="background-color:${car.color}"></td>
                            </tr>`;

    });
    let anchors = document.querySelectorAll('a');
    
    anchors.forEach(function(link){
        let anchorId = link.id;
        let url = localhost + "/search/" + anchorId;
        link.addEventListener('click', function(){
            ajax('GET', url, createTable);
        });
    });
};

let quickSearchField = document.querySelector('#quickSearch');

quickSearchField.addEventListener('keyup', function(e){
    console.log(quickSearchField.value);
    let url = localhost + "/search?plate=" + quickSearchField.value;
    ajax('GET', url, createTable);
});

let showCreatePanelButton = document.querySelector('#showCreatePanel');
let panel = document.querySelector('.newrecords');

showCreatePanelButton.addEventListener('click', function () {
    panel.style.display = 'inline-block';
});

let saveButton = document.querySelector('.save');
saveButton.addEventListener('click', function(){
    panel.style.display = 'none';
    let plateField = document.querySelector('#plate');
    let brandField = document.querySelector('#brand');
    let modelField = document.querySelector('#model');
    let colorField = document.querySelector('#color');
    let yearField = document.querySelector('#year');
    
    let url = localhost + "/add?plate=" + plateField.value + "&brand=" + brandField.value
    + "&model=" + modelField.value + "&color=" + colorField.value + "&year=" + yearField.value;
    
    if (plateField.value === "" || brandField.value === "" || modelField.value === "" || colorField.value === "" || yearField.value === ""){
        url = localhost;
    };
    
    ajax('GET', url, createTable);
});