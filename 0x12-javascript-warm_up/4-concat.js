#!/usr/bin/node
/* prints 2 arguments passed to it, format: "is" */
const args = process.argv.slice(2);
console.log(`${args[0]} is ${args[1]}`);
