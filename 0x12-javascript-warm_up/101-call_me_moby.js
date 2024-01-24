#!/usr/bin/node

/**
 * Executes a function x times
 * @param {number} x - Number of times to execute the function
 * @param {Function} theFunction - The function to be executed
 */
function executeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Example usage:
const myFunction = () => console.log('Executing the function!');
executeXTimes(5, myFunction);
