var firstParagraph = document.querySelector('p');

var output1 = document.querySelector('.output1');
var output2 = document.querySelector('.output2');

output1.textContent = firstParagraph.textContent;
output2.innerHTML = firstParagraph.innerHTML;
