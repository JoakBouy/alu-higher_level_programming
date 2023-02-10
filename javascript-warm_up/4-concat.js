#!/usr/bin/node
const args = require('process').argv;
let firstArg = args.slice(2, 3).toString();
let secondArg = args.slice(3, 4).toString();

if (!firstArg) firstArg = undefined;
if (!secondArg) secondArg = undefined;

console.log(`${firstArg} is ${secondArg}`);
