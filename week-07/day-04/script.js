var imageCounter = 1;
var imageTotal = 5;

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

var leftButton = document.querySelector('.left-button');
var rightButton = document.querySelector('.right-button');

var slideImageLeft = function() {
  slideImage(-1);
};

var slideImageRight = function() {
  slideImage(1);
}

leftButton.addEventListener('click', slideImageLeft);
rightButton.addEventListener('click', slideImageRight);
