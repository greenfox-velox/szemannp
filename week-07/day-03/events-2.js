var listContainer = document.querySelectorAll('ul li');
var result = document.querySelector('.result');

function getListLength() {
  result.textContent = listContainer.length;
}

var button = document.querySelector('button');
button.addEventListener('click', getListLength);
