var imageUrl = document.querySelector('img');
var link = document.querySelector('a');
var buttonToChange = document.querySelector('.this-one');

console.log(imageUrl);

imageUrl.src = './myself_resized.png';
link.href = 'http://www.greenfoxacademy.com';
buttonToChange.disabled = true;
buttonToChange.textContent = 'Don\'t click me';
