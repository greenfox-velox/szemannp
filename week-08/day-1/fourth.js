'use strict';

var carId = 0;
var price = 40;
var index = 0;

function Car(type, color, balance) {
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.ownId = carId++;
}

Car.prototype.enter = function (enterDate) {
  this.enterDate = enterDate;
};

Car.prototype.getStats = function () {
  return 'Type: ' + this.type + ', Color: ' + this.color + ', Balance: ' + this.balance + ', id: ' + this.ownId;
};

Car.prototype.getEnterDate = function () {
  return this.enterDate;
};

Car.prototype.leave = function (price) {
  this.balance -= price;
};


// Test objects:

var tesla = new Car('Tesla', 'black', 700);
var volvo = new Car('Volvo', 'blue', 550);

// Test calls:

volvo.enter(5000);
tesla.enter(3000);

console.log(tesla);
console.log(volvo);
console.log(tesla.getStats());
console.log(volvo.getStats());
console.log('enter date is: ' + volvo.getEnterDate());

// ***********************       CarPark part

function CarPark(income, startTime) {
  this.income = income;
  this.startTime = startTime;
  this.feePerHour = 40;
  this.parkingLot = {};
}

CarPark.prototype.carEnter = function (car) {
  this.parkingLot[car.ownId] = car;
  console.log('this is inside the car container object: ' + this.parkingLot);
};

CarPark.prototype.getStats = function () {
  return 'Cars: ' + this.parkingLot.length + ', Income: ' + this.income;
};

CarPark.prototype.carLeave = function (id) {
  delete this.parkingLot[id];
};

// Test objects

var myLot = new CarPark(3800, 0);

// Test calls

myLot.carEnter(volvo);
myLot.carEnter(tesla);

console.log(myLot.parkingLot);
console.log(myLot.getStats());

myLot.carLeave(0);
console.log(myLot.parkingLot);

// CarPark.prototype.elapseTime = function (hours) {
//
// };
//

// };
//
// CarPark.prototype.getParkingCarsSince = function (hours) {
//   return
//
// };
