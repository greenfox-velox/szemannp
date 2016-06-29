var asteroids = [];
var parent = document.querySelector('ul.asteroids');

var asteroidList = function(array) {
  for (i = 0; i < array.length; i++) {
    if (array[i].asteroid) {
      asteroids.push(array[i]);
    }
  }
  return asteroids;
};

asteroidList(planetData);
console.log(asteroids);

for (i = 0; i < asteroidList.length; i++) {
  asteroids[i].class = asteroids[i].category;
  asteroids[i].textContent = asteroids[i].content;
}


for (i = 0; i < asteroids.length; i++) {
  var newItem = asteroids[i];
  parent.appendChild(newItem);
}
