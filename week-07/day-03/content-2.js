// var apple = document.querySelector('.apple');
// var banana = document.querySelector('.balloon');
// var car = document.querySelector('.cat');
// var dolphin = document.querySelector('.dog');
//
// apple.textContent = dolphin.textContent;
// console.log(apple);

var paragraphContainer = document.querySelectorAll('p');

for (i = 0; i < paragraphContainer.length; i++) {
  paragraphContainer[i].textContent = paragraphContainer[3].textContent;
}

console.log(paragraphContainer);
