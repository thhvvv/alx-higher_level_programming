#!/usr/bin/node
/* prints the number of arguments already printed and new argument value */
let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
