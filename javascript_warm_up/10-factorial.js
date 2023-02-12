#!/usr/bin/node
const args = require('process').argv;
const inputInt = args.slice(2, 3);

function factorial (a) {
  if (!a || a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const a = Number(inputInt);

console.log(factorial(a));
