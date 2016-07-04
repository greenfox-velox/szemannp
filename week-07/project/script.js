'use strict';

var mainImage = document.querySelector('.main');

var nextImageButton = document.querySelector('.next-image');
var previousImageButton = document.querySelector('.previous-image');

var nextThumbsetButton = document.querySelector('.next-thumbset');
var previousThumbsetButton = document.querySelector('.previous-thumbset');

var thumbPics = document.querySelectorAll('.thumbnailpic');

var imageFolder = 'img/pics/';
var listOfImages = ['img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg', 'img_5.jpg', 'img_6.jpg', 'img_7.jpg', 'img_8.jpg', 'img_9.jpg', 'img_10.jpg', 'img_11.jpg', 'img_12.jpg', 'img_13.jpg'];

var currentImageIndex = 0;
var currentThumbIndex = 0;

function setDisplayedImage(imageIndex) {
  return imageFolder + listOfImages[imageIndex];
}

function changeMainImage(displayedImage) {
  mainImage.setAttribute('src', displayedImage);
}

function setThumbnailTile(index) {
  thumbPics[2].setAttribute('src', setDisplayedImage(index));
  if(index === 0) {
    thumbPics[1].setAttribute('src', setDisplayedImage(listOfImages.length - 1));
    thumbPics[0].setAttribute('src', setDisplayedImage(listOfImages.length - 2));
  } else if(index === 1) {
    thumbPics[1].setAttribute('src', setDisplayedImage(0));
    thumbPics[0].setAttribute('src', setDisplayedImage(listOfImages.length - 1));
  } else {
    thumbPics[1].setAttribute('src', setDisplayedImage(index - 1));
    thumbPics[0].setAttribute('src', setDisplayedImage(index - 2));
  }

  if (index === listOfImages.length -1) {
    thumbPics[3].setAttribute('src', setDisplayedImage(0));
    thumbPics[4].setAttribute('src', setDisplayedImage(1));
  } else if(index === listOfImages.length -2) {
    thumbPics[3].setAttribute('src', setDisplayedImage(listOfImages.length - 1));
    thumbPics[4].setAttribute('src', setDisplayedImage(0));
  } else {
    thumbPics[3].setAttribute('src', setDisplayedImage(index + 1));
    thumbPics[4].setAttribute('src', setDisplayedImage(index + 2));
  }
}

function changeNext() {
  if (currentImageIndex < listOfImages.length - 1) {
    currentImageIndex += 1;
    currentThumbIndex += 1;
    changeMainImage(setDisplayedImage(currentImageIndex));
    setThumbnailTile(currentImageIndex);
  } else {
    currentImageIndex = 0;
    currentThumbIndex = 0;
    changeMainImage(setDisplayedImage(currentImageIndex));
    setThumbnailTile(currentImageIndex);
  }
}

function changePrevious() {
  if (currentImageIndex > 0) {
    currentImageIndex -= 1;
    currentThumbIndex -= 1;
    changeMainImage(setDisplayedImage(currentImageIndex));
    setThumbnailTile(currentImageIndex);
  } else {
    currentImageIndex = listOfImages.length - 1;
    currentThumbIndex = listOfImages.length - 1;
    changeMainImage(setDisplayedImage(currentImageIndex));
    setThumbnailTile(currentImageIndex);
  }
}

function changeThumbNext() {
  if (currentThumbIndex < listOfImages.length - 1) {
    currentThumbIndex += 1;
    setThumbnailTile(currentThumbIndex);
  } else {
    currentThumbIndex = 0;
    setThumbnailTile(currentThumbIndex);
  }
}

function changeThumbPrevious() {
  if (currentThumbIndex > 0) {
    currentThumbIndex -= 1;
    setThumbnailTile(currentThumbIndex);
  } else {
    currentThumbIndex = listOfImages.length - 1;
    setThumbnailTile(currentThumbIndex);
  }
}

nextImageButton.addEventListener('click', changeNext);
previousImageButton.addEventListener('click', changePrevious);

nextThumbsetButton.addEventListener('click', changeThumbNext);
previousThumbsetButton.addEventListener('click', changeThumbPrevious);

window.addEventListener('keypress', onSpacePressed);

mainImage.setAttribute('src',setDisplayedImage(currentImageIndex));
setThumbnailTile(currentImageIndex);

function onSpacePressed()
{
    var keyPressed = event.keyCode || event.which;
    if(keyPressed==32) {
        changeNext();
        keyPressed=null;
    }
}
