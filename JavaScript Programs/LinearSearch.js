// Write your code below this line
function linearSearch(searchTerm, arr) {
   for (let i = 0; i < arr.length; i++) {
    if (arr[i] === searchTerm) {
      return i;
    }
  }
  return undefined;
}

function globalLinearSearch(searchTerm, arr) {
  const indices = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === searchTerm) {
      indices.push(i);
    }
  }
  return indices;
}

// Helper function to compare arrays
function arraysEqual(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

// DO NOT MODIFY THE TEST CODE BELOW
// Test cases for linearSearch
console.log(linearSearch(1, [1, 2, 3]) === 0); // linearSearch(1, [1, 2, 3]) should be 0
console.log(linearSearch(3, [1, 2, 3]) === 2); // linearSearch(3, [1, 2, 3]) should be 2
console.log(linearSearch(4, [1, 2, 3]) === undefined); // linearSearch(4, [1, 2, 3]) should be undefined

// Test cases for globalLinearSearch
console.log(arraysEqual(globalLinearSearch("a", "bananas".split("")), [1, 3, 5])); // globalLinearSearch('a', 'bananas'.split('')) should be [1, 3, 5]
console.log(arraysEqual(globalLinearSearch("s", "bananas".split("")), [6])); // globalLinearSearch('s', 'bananas'.split('')) should be [6]
console.log(arraysEqual(globalLinearSearch("n", "bananas".split("")), [2, 4])); // globalLinearSearch('n', 'bananas'.split('')) should be [2, 4]

