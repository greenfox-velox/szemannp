var asteroids = document.querySelector('ul.asteroids');
var newListItemFox = document.createElement('li');
var newListItemLamp = document.createElement('li');

newListItemFox.textContent = 'The Green Fox';
newListItemLamp.textContent = 'The Lamplighter';
asteroids.appendChild(newListItemFox);
asteroids.appendChild(newListItemLamp);

var container = document.querySelector('.container');
var newHeading = document.createElement('h1');
var newImage = document.createElement('img');

newHeading.textContent = 'I can add elements to the DOM';
newImage.src = './myself_resized.png';

container.appendChild(newHeading);
container.appendChild(newImage);
