#!/usr/bin/node
const args = require('process').argv;
const argPassed = args.slice(2, 3);
let checkNaN = Number(argPassed);

if (argPassed.length === 0 || isNaN(checkNaN)) {
  console.log('Missing number of occurrences');
} else {
  while (checkNaN > 0) {
    console.log('C is fun');
    checkNaN--;
  }
}
