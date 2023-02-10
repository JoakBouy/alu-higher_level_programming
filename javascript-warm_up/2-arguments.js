#!/usr/bin/node
const commands = require('process');
const length = commands.argv.length;

if (length > 3) {
  console.log('Arguments found');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
