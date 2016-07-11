'use strict';

var xhr = new XMLHttpRequest();
var todos = [];
var listShell = document.querySelector('.todos-container');
var addButton = document.querySelector('.add');
var inputField = document.querySelector('.input');

function createBlock(element) {
  var newBlock = document.createElement('div');
  var buttonBlock = document.createElement('div');
  var newDelButton = document.createElement('img');
  var newCompletedButton = document.createElement('img');
  var newListItem = document.createElement('label');
  listShell.appendChild(newBlock);
  newBlock.appendChild(newListItem);
  newBlock.appendChild(buttonBlock);
  buttonBlock.appendChild(newDelButton);
  buttonBlock.appendChild(newCompletedButton);
  newBlock.id = element.id;
  newBlock.className = 'list-item';
  buttonBlock.className = 'button-block';
  newDelButton.src = 'bin.png';
  newDelButton.className = 'del list-button';
  if (element.completed) {
    newCompletedButton.src = 'checked.png';
  } else {
    newCompletedButton.src = 'unchecked.png';
  }
  newCompletedButton.className = 'status list-button' + ' ' + 'i' + element.id;
  newListItem.textContent = element.text;
  newListItem.className = 'todo-item';
  newListItem.completed = 'false';
}

function processResponse(response) {
  for (var i = 0; i < response.length; i++) {
    if (response[i].text.length > 0) {
      createBlock(response[i]);
    }
  }
}

function sendRequest() {
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr.responseType = 'json';
  xhr.send();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      if (xhr.status === 200 || 201 || 202 || 304 ) {
        todos = xhr.response;
        processResponse(todos);
      } else {
        console.log('Error: ' + xhr.status);
      }
    }
  };
}

function addTodoItem() {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  var toAdd = document.querySelector('input').value;
  var toAddValue = { "text": toAdd };
  xhr.onload = function(){
    var todos = xhr.response;
    console.log(todos);
    createBlock((todos[todos.length - 1].id) + 1);
  };
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(toAddValue));
  xhr.onload = function(){
    window.location.reload();
  };
}

function removeItem(toRemoveId) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function(){
    console.log(id);
    listShell.removeChild(toRemoveId);
  };
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + toRemoveId, true);
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
  var toSet = document.querySelector('.i' + id);
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
  xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(updateStatus));
  xhr.onload = function() {
    window.location.reload();
  };
}

addButton.addEventListener('click', addTodoItem);
listShell.addEventListener('click', eventHandler);

window.onload = sendRequest;
