#!/usr/bin/node
/* prints certain amount of times of string */
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
	console.log('Missing number of occurences');
}
else if (x > 0) {
	for (let i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
