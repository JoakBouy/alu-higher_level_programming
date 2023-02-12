#!/usr/bin/node
const args = require('process').argv;
const argPassed = args.slice(2, 3).toString();

if (argPassed) {
  console.log(argPassed);
} else {
  console.log('No argument');
}
