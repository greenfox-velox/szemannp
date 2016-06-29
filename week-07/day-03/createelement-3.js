var listOfItems = ['apple', 'bubble', 'cat', 'green fox'];
var parent = document.querySelector('ul.asteroids');
var toRemove = document.querySelector('li');

parent.removeChild(toRemove);

for (i = 0; i < listOfItems.length; i++) {
  var newItem = document.createElement('li');
  newItem.textContent = listOfItems[i];
  parent.appendChild(newItem);
}
