#!/usr/bin/node
/* function that increments and calls a function */
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
