#!/usr/bin/node
/* prints script if first argument can be converted to an integer */
const value = parseInt(process.argv[2]);
if (isNaN(value)) {
	console.log('Not a number');
}
else {
	console.log(`My number: ${value}`);
}
