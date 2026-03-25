// Write your code below this line
function fibonacci(num) {
  if (num === 0) return 0;
  if (num === 1) return 1;

  let prev = 0;  // F(0)
  let curr = 1;  // F(1)

  for (let i = 2; i <= num; i++) {
    const next = prev + curr; // F(n) = F(n-1) + F(n-2)
    prev = curr;
    curr = next;
  }

  return curr;
}


// DO NOT MODIFY THE TEST CODE BELOW
// Test cases
console.log(fibonacci(0) === 0);  // fibonacci(0) should be 0
console.log(fibonacci(2) === 1);  // fibonacci(2) should be 1
console.log(fibonacci(5) === 5);  // fibonacci(5) should be 5
console.log(fibonacci(8) === 21); // fibonacci(8) should be 21
console.log(fibonacci(11) === 89); // fibonacci(11) should be 89