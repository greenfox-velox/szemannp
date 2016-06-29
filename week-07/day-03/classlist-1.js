var paragraphContainer = document.querySelectorAll('p');

if (paragraphContainer[2].classList.contains('cat')) {
  alert('YEAH CAT!');
}

if (paragraphContainer[3].classList.contains('dolphin')) {
  paragraphContainer[0].textContent = 'pear';
}

if (paragraphContainer[0].classList.contains('apple')) {
  paragraphContainer[2].textContent = 'dog';
}

paragraphContainer[0].classList.add('red');
paragraphContainer[1].classList.toggle('balloon');
