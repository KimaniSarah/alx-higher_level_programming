#!/usr/bin/node

const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
function add (a, b) {
  const result = a + b;
  console.log(result);
}
if (!isNaN(a) && !isNaN(b)) {
  add(a, b);
} else {
  console.log('NaN');
}
