#!/usr/bin/node

/**
 * Increments a number and calls a function
 * @param {number} number - The number to be incremented
 * @param {Function} theFunction - The function to be called
 */
function incrementAndCall(number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
}
