#!/usr/bin/node
const args = require('process').argv;
const argPassed = args.slice(2, 3);
const checkNaN = Number(argPassed);

if (argPassed.length === 0 || isNaN(checkNaN)) {
  console.log('Missing size');
} else {
  let tmp = checkNaN;
  let inner = 0;
  let s = '';

  while (tmp > 0) {
    while (inner < checkNaN) {
      s += 'X';
      inner++;
    }
    console.log(s);
    tmp--;
  }
}
