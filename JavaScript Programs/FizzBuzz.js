/*
FizzBuzz
Write a program that uses console.log to print all the numbers from 1 to 100, with two exceptions. For numbers divisible by 3, print "Fizz" instead of the number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.

When you have that working, modify your program to print "FizzBuzz" for numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz" for numbers divisible by only one of those).

(This is actually an interview question that has been claimed to weed out a significant percentage of programmer candidates. So if you solved it, your labor market value just went up.)

Going over the numbers is clearly a looping job, and selecting what to print is a matter of conditional execution. Remember the trick of using the remainder (%) operator for checking whether a number is divisible by another number (has a remainder of zero).

In the first version, there are three possible outcomes for every number, so you’ll have to create an if/else if/else chain.

The second version of the program has a straightforward solution and a clever one. The simple solution is to add another conditional “branch” to precisely test the given condition. For the clever solution, build up a string containing the word or words to output and print either this word or the number if there is no word, potentially by making good use of the || operator.

*/

//Original solution
for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}


//Clever solution
for (let n = 1; n <= 100; n++) {
  let output = "";
  if (n % 3 == 0) output += "Fizz";
  if (n % 5 == 0) output += "Buzz";
  console.log(output || n);
}

/*
The clever solution builds up a string by adding "Fizz" if the number is divisible by 3 and "Buzz" if it is divisible by 5. If the number is not divisible by either, the string will be empty, and the || operator will cause the number itself to be printed.

This solution is more concise and arguably easier to read, as it avoids the nested if/else structure of the original solution. It also demonstrates a common pattern in programming where you build up a result incrementally and then use a fallback value if the result is empty or falsy.

console.log(output || n); means the following:

The variable output starts as an empty string.

If n is divisible by 3, "Fizz" is appended to output.

If n is divisible by 5, "Buzz" is appended to output.

If n is divisible by both 3 and 5, output becomes "FizzBuzz".

The logical OR operator (||) is then used to print output if it is a non-empty string (truthy value).

If output is still empty (falsy), meaning n was neither divisible by 3 nor 5, it prints the number n itself.

So, console.log(output || n); is a concise way of saying: print the output string if any conditions for "Fizz" or "Buzz" were met; otherwise, print the number itself. This avoids the need for an explicit if-else statement to check whether output is empty ​. It results in cleaner, shorter code while maintaining the full correct behavior of FizzBuzz.

In summary, this line ensures that each number or its corresponding "Fizz", "Buzz", or "FizzBuzz" is printed appropriately, fully implementing the FizzBuzz logic in a neat and clever way.
*/