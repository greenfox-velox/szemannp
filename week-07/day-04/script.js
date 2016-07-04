var imageCounter = 1;
var imageTotal = 5;
var leftButton = document.querySelector('.left-button');
var rightButton = document.querySelector('.right-button');
var heading = document.querySelector('h1');

function slideImage(direction) {
  var image = document.querySelector('#image');
  console.log(image);
  imageCounter = imageCounter + direction;
  if (imageCounter > imageTotal) {
    imageCounter = 1;
  }
  if (imageCounter < 1) {
    imageCounter = imageTotal;
  }
  image.src = 'images/img_' + imageCounter + '.jpg';
}

var changeHeading = function() {
  var userInput = prompt('Name your picture gallery!');
  if (userInput.length < 1) {
    userInput = 'Anon\'s gallery';
  }
  heading.textContent = userInput;
}

var slideImageLeft = function() {
  slideImage(-1);
};

var slideImageRight = function() {
  slideImage(1);
}

leftButton.addEventListener('click', slideImageLeft);
rightButton.addEventListener('click', slideImageRight);
heading.addEventListener('click', changeHeading);
