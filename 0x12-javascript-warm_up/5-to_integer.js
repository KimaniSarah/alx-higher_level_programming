#!/usr/bin/node

const arg = process.argv[2];
const argAsInt = parseInt(arg);
if (!isNaN(argAsInt)) {
  console.log(`My number: ${argAsInt}`);
} else {
  console.log('Not a number');
}
