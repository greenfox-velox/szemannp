var asteroids = [];
var parent = document.querySelector('ul.asteroids');
var child = document.querySelector('li');

parent.removeChild(child);

planetData.forEach(function (e) {
   if (e['asteroid']) {
     var newLi = document.createElement('li');
     newLi.textContent = e['content'];
     newLi.classList.add(e['category']);
     parent.appendChild(newLi);
   }
 });
