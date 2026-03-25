// Write your code below this line
function factorial(num) {
  if (num < 0) return undefined;
  let result = 1;

  for (let i = 2; i <= num; i++) {
    result *= i;
  }

  return result;
}


// DO NOT MODIFY THE TEST CODE BELOW
// Test cases
console.log(factorial(0) === 1); // factorial(0) should be 1
console.log(factorial(1) === 1); // factorial(1) should be 1
console.log(factorial(2) === 2); // factorial(2) should be 2
console.log(factorial(4) === 24); // factorial(4) should be 24
console.log(factorial(8) === 40320); // factorial(8) should be 40320
console.log(factorial(18) === 6402373705728000); // factorial(18) should be 6402373705728000
// Test how high of a number your program can calculate. Can you push it further?
