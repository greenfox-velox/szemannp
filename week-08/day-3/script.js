var xhr = new XMLHttpRequest();

var buttonClick = function() {
  console.log(JSON.parse(xhr.response));
};

xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2015/9/27')
xhr.send();

var siteButton = document.querySelector('.clickme');
siteButton.addEventListener('click', buttonClick);
