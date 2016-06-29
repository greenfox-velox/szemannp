var toListItems = ['apple', 'banana', 'cat', 'dog'];
var htmlList = document.querySelectorAll('li');

for (i = 0; i < htmlList.length; i++) {
  htmlList[i].textContent = toListItems[i];
}
