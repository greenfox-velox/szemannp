'use strict';

var express = require('express');
var mysql = require('mysql');
var http = require('http');

var con = mysql.createConnection ({
  host: 'localhost',
  user: 'root',
  password: 'solar``7',
  database: 'bookstore'
});

con.connect(function (err) {
  if (err) {
    console.log('Error connecting to DataBase');
    return;
  }
  console.log('Connection established');
});


var queryBookNames = con.query('select aut_name from author', function (err, result){
  if (err) {
    console.log(err.toString());
  }
  console.log('Data recieved from DB:\n');
  console.log(result);
});
