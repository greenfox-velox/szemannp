var listToChange = document.querySelector('ul.asteroids');
console.log(listToChange);

var childToRemove = document.querySelector('li');

listToChange.removeChild(childToRemove);

for (i = 0; i < 3; i++) {
  var newItem = document.createElement('li');
  newItem.textContent = 'The Fox';
  newItem.id = i;
  listToChange.appendChild(newItem);
}
