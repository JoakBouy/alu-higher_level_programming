#!/usr/bin/node
const args = require('process').argv;
const argPassed = args.slice(2, 3);
const checkNaN = Number(argPassed);

argPassed.length === 0 || isNaN(checkNaN)
  ? console.log('Not a number')
  : console.log(`My number: ${Number(argPassed)}`);
