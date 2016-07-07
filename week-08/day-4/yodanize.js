'use strict';

var siteButton = document.querySelector('.toClick');
var textContainer = document.querySelector('.input');
var resultContainer = document.querySelector('.displayResult');
var xhr = new XMLHttpRequest();
var message = textContainer.value;


function sendRequest() {
  xhr.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(textContainer.value), true);
  xhr.setRequestHeader("X-Mashape-Authorization", "hBwzI4sy4omsh6rO62VDfAq4mcXip1N8YEsjsnZ7mdxPB3vdE4");
  xhr.send();
  xhr.onload = function() {
    resultContainer.innerText = xhr.responseText;
  }
}

siteButton.addEventListener('click', sendRequest);
