#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);
if (!isNaN(args[2])) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
