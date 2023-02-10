#!/usr/bin/node
const args = require('process').argv.slice(2);

if (!args.length || args.length === 1) {
  console.log(0);
} else {
  let biggest = 0;
  let secondBiggest = 0;
  let x;
  let y;

  for (x = 0; x < args.length; x++) {
    if (Number(args[x]) > biggest) {
      biggest = Number(args[x]);
    }
  }

  for (y = 0; y < args.length; y++) {
    if (Number(args[y]) > secondBiggest && Number(args[y]) < biggest) {
      secondBiggest = Number(args[y]);
    }
  }
  console.log(secondBiggest);
}
