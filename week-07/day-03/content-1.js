var heading = document.querySelector('h1').textContent;
alert(heading);

var firstParagraph = document.querySelector('p').textContent;
console.log(firstParagraph);

var secondParagraph = document.querySelector('.other').textContent;
alert(secondParagraph);

var newContent = 'New content';
heading = newContent;
alert(heading);

var lastParagraph = document.querySelector('.result').textContent;
lastParagraph = firstParagraph;
console.log(lastParagraph);
