let images = [{
    'title': 'elso kep',
    'description': "ide sok szoveg jon",
    'url': "https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/1909758_705557362917651_5561632227437550336_n.jpg?oh=ce445a4b1be3161f7b8ff5424f090393&oe=5AA95D3B"
},
{
    'title': 'masodik kep',
    'description': 'sok-sok szoveg',
    'url': "https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/10325619_705557152917672_4269124930293393731_n.jpg?oh=36550dc35c38655bab9525c1f5d94216&oe=5A7F5A15"
},
{
    'title': 'legujabb kep',
    'description': 'okokokokok',
    'url': "https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/10523761_705556302917757_3946690819798907681_n.jpg?oh=5208701daf2aad4489afca3f136f8269&oe=5A6ADF31"
},
{
    'title': 'utolso kep',
    'description': 'blablabla',
    'url': "https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/12074771_644368269036561_4957046902188976204_n.jpg?oh=19ac6fce53c5331a0d82f8ad01ad7525&oe=5AAAC78B"
}
];


function renderThumbs(list) {
    for (let imgIterator = 0; imgIterator < list.length; imgIterator++) {
        console.log(images[imgIterator]['title']);
    }
    let thumbnail = document.querySelector('.thumbnail');
    for (let i = 0; i < list.length; i++) {
        let newListElement = document.createElement('img');
        thumbnail.appendChild(newListElement);
        newListElement.textContent = list[i]['title'];
        var imgSrc = list[i]['url'];
        newListElement.setAttribute('src', imgSrc);
    }
}

function renderImage (img) {
    let container = document.querySelector('.bigpic');
    container.addEventListener('click');

}


renderThumbs(images);

renderImage();