var allH1 = document.querySelectorAll('h1');
for (var i = 0; i < allH1.length; i++) {
  var msgToWrld = prompt('Send your message to the world!');
  allH1[i].textContent = msgToWrld;
}
