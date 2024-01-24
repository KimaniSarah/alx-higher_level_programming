#!/usr/bin/node

/**
 * Increments a number and calls a function
 * @param {number} number - The number to be incremented
 * @param {Function} theFunction - The function to be called
 */
function incrementAndCall (number, theFunction) {
  const incr = (x) => x + 1; // New function incr that increments the integer value
  const incrementedNumber = incr(number);
  theFunction(incrementedNumber);
}
