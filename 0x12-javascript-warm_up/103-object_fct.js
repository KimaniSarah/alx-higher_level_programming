#!/usr/bin/node

/**
 * Increments a number and calls a function
 * @param {number} number - The number to be incremented
 * @param {Function} theFunction - The function to be called
 */
function incrementAndCall (number, theFunction) {
  const incr = (x) => x + 1;
  const incrementedNumber = incr(number);
  theFunction(incrementedNumber);
}
const myFunction = (result) => console.log(`The incremented number is ${result}`);
incrementAndCall(5, myFunction);
