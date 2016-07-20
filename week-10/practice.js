'use strict';

// non-arrow factory

var dog = function () {
  var sound = 'woof';

  return {
    talk: function () {
      console.log(sound);
    }
  }
};

var blokie = dog();
blokie.talk();

// module pattern

var dogModule = (function () {

  var sound = 'woofie';

  return {
    talk: function () {
      console.log(sound);
    }
  }
}) ();

dogModule.talk();

// revealing module pattern

var dogRevealing = (function() {
  var privateSound = 'woofers';
  var privateTalk = function () {
    console.log(privateSound);
  };
  return {
    publicTalk: privateTalk
  };
}) ();

dogRevealing.publicTalk();


// constructor + prototype

var Dog = function () {
  this.sound = 'woofin';
};

Dog.prototype.talk = function () {
  console.log(this.sound);
};

var zsele = new Dog();
zsele.talk();
