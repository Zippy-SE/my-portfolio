// Write your code below this line
function toRomanLazy(num) {
    const map = [
    [1000, "M"],
    [500, "D"],
    [100, "C"],
    [50, "L"],
    [10, "X"],
    [5, "V"],
    [1, "I"],
  ];

  let result = "";
  for (const [value, symbol] of map) {
    while (num >= value) {
      result += symbol;
      num -= value;
    }
  }
  return result;
}


function toRoman(num) {
   const map = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];

  let result = "";
  for (const [value, symbol] of map) {
    while (num >= value) {
      result += symbol;
      num -= value;
    }
  }
  return result;
}

// DO NOT MODIFY THE TEST CODE BELOW
// Test cases for toRomanLazy
console.log(toRomanLazy(4) === "IIII"); // toRomanLazy(4) should be 'IIII'
console.log(toRomanLazy(150) === "CL"); // toRomanLazy(150) should be 'CL'
console.log(toRomanLazy(944) === "DCCCCXXXXIIII"); // toRomanLazy(944) should be 'DCCCCXXXXIIII'

// Test cases for toRoman (modern)
console.log(toRoman(4) === "IV"); // toRoman(4) should be 'IV'
console.log(toRoman(150) === "CL"); // toRoman(150) should be 'CL'
console.log(toRoman(944) === "CMXLIV"); // toRoman(944) should be 'CMXLIV'
