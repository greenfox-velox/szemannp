'use strict';

var xhr = new XMLHttpRequest();
var listShell = document.querySelector('.todos-container');
var addButton = document.querySelector('.add');
var inputField = document.querySelector('.input');

function createBlock(element) {
  var newBlock = document.createElement('div');
  newBlock.id = '#i' + element.id;
  newBlock.classList.add('list-item');
  var buttonBlock = document.createElement('div');
  buttonBlock.classList.add('button-block');
  var newDelButton = document.createElement('img');
  newDelButton.src = 'bin.png';
  newDelButton.className = 'del list-button';
  var newCompletedButton = document.createElement('img');
  var newListItem = document.createElement('label');
  listShell.appendChild(newBlock);
  newBlock.appendChild(newListItem);
  newBlock.appendChild(buttonBlock);
  buttonBlock.appendChild(newDelButton);
  buttonBlock.appendChild(newCompletedButton);
  if (element.completed) {
    newCompletedButton.src = 'checked.png';
  } else {
    newCompletedButton.src = 'unchecked.png';
  }
  newCompletedButton.className = 'status list-button';
  newListItem.textContent = element.text;
  newListItem.classList.add('todo-item');
  newListItem.completed = 'false';
}

function processResponse(response) {
  var processedResponse = JSON.parse(response);
  for (var i = 0; i < processedResponse.length; i++) {
    if (processedResponse[i].text.length > 0) {
      createBlock(processedResponse[i]);
    }
  }
}

function sendRequest() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://localhost:3000/todos/', true);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  xhr.send('');
  xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
      processResponse(xhr.response);
    }
  }
}

function addTodoItem() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:3000/todos/', true);
  var toAdd = document.querySelector('input').value;
  var toAddValue = { "text": toAdd };
  xhr.onload = function(){
    var todos = xhr.response;
    console.log(todos);
    createBlock((todos[todos.length - 1].id) + 1);
  };
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify({ text: inputdata.value} ));
  xhr.onload = function(){
    window.location.reload();
  };
}

function removeItem(toRemoveId) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function(){
    console.log(toRemoveId);
    listShell.removeChild(toRemoveId);
  };
  xhr.open('DELETE', 'http://localhost:3000/todos/' + toRemoveId, true);
  xhr.setRequestHeader('accept', 'application/json');
  xhr.send();
  xhr.onload = function() {
    window.location.reload();
  };
}

function eventHandler() {
  var toRe = event.target.classList.contains('i' + event.target.parentElement.parentElement.parentElement.id)
  console.log(toRe);
  if (event.target.classList.contains('status')) {
    setCheckbox(event.target.parentElement.parentElement.id);
  }
  else if (event.target.classList.contains('del')) {
    removeItem(event.target.parentElement.parentElement.id);
  }
}

function setCheckbox(id){
  var toSet = document.querySelector('#i' + id);
  toSet.src = 'checked.png';
  console.log(toSet);
  var updateStatus = {
    completed: true
  }
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var todos = xhr.response;
    processResponse(todos);
  };
  xhr.open('PUT', 'http://localhost:3000/todos/' + id);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(updateStatus));
  xhr.onload = function() {
    window.location.reload();
  };
}

window.onload = sendRequest();

addButton.addEventListener('click', addTodoItem);
listShell.addEventListener('click', eventHandler);
