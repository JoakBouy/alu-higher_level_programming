#!/usr/bin/node
const args = require('process').argv;
const firstInt = args.slice(2, 3);
const secondInt = args.slice(3, 4);

function add (a, b) {
  if (!a || !b) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}

const a = Number(firstInt);
const b = Number(secondInt);

add(a, b);
