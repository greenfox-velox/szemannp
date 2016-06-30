
function startToParty() {
    var buttonToResize = document.querySelector('div');
    buttonToResize.classList.toggle('party');
}

var buttonToSwitch = document.querySelector('button');
buttonToSwitch.addEventListener('click', startToParty);
