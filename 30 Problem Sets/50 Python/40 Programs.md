# Zeller's Algorithm

Zeller's algorithm computes the day of the week on which a given date will fall
(or fell). In this exercise, you will write a program to run Zeller's algorithm
on a specific date. You will need to create a new file for this program,
`zellers.py`. The program should use the algorithm outlined below to compute the
day of the week on which the user's birthday fell in the year you were born and
print the result to the screen.

Write a function (zellers) that takes parameters (month, day, year), and uses dictionaries to facilitate "pretty printing" (where the answer is given to the user in a nice looking
fashion).

Calling `zellers("March", 10, 1940)` should give the output: `Sunday`.

Zeller's algorithm is defined as follows:

Let A, B, C, D denote integer variables that have the following values:

* `A` = the month of the year, with March having the value 1, April the value 2,
  ..., December the value 10, and January and February being counted as months
  11 and 12 of the preceding year (in which case,subtract 1 from C)
* `B` = the day of the month (1, 2, 3, . . . , 30, 31)
* `C` = the year of the century (e.g. C = 89 for the year 1989)
* `D` = the century (e.g. D = 19 for the year 1989)

Note: if the month is January or February, then the preceding year is used for
computation. This is because there was a period in history when March 1st, not
January 1st, was the beginning of the year.

Let W, X, Y, Z, R also denote integer variables. Compute their values in the
following order using integer arithmetic:

* `W = (13 * A - 1) / 5`
* `X = C / 4`
* `Y = D / 4`
* `Z = W + X + Y + B + C - 2 * D`
* `R = the remainder when Z is divided by 7`
	
The value of R is the day of the week, where 0 represents Sunday, 1 is Monday,
..., 6 is Saturday. If the computed value of R is a negative number, add 7 to
get a non negative number between 0 and 6. You can check to be sure your code is working by looking at [timeanddate.com](http://www.timeanddate.com/calendar/).

Provide atleast three test cases at the bottom of the file: try today's date, your birth date, and whatever else interests you!

Hints:

1. Use a dictionary to map between the month and its numerical value.

2. You can use either a list or dictionary to convert the final output of the
   algorithm to the day of the week.

3. Make sure you handle the following three points correctly.

   * Note: If the month is January or February, then the preceding year is
     used for computation. This is because there was a period in history when
     March 1st, not January 1st, was the beginning of the year.

   * If the computed value of R is a negative number, add 7 to get a
     nonnegative number between 0 and 6.

   * You might need to use one of the following (but, maybe not): To convert
     the string '90' to the number 90, use `int('90')`; to convert the int 90 to
     the string '90', use `str(90)`.

# Hacker addition: List comprehensions

List comprehensions follow naturally from set builder notation and lambda calculus. They are very cool and make your life a lot easier. Don't worry if you don't get them yet.

Read about list comprehensions on pages 34-35 of the 6.01 [course notes]; the Wikipedia article on them are good, and [this site] is concise and good.

Put this program in `comprehensions.py`.

1. Write a list comprehension that prints a list of the cubes of the numbers 1 through 10.

2. Write a list comprehension that prints out the possible results of two coin flips (one result would be 'ht'). (Hint - how many results should there be?)

3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.

4. Write a function that takes in a list of elements of different types and uses a list comprehension to return all the elements of the list of type int. Note: The function isinstance will be of help here. Google "Python isinstance" and see if you can figure out what it does, or type help(isinstance) at the Python shell.

5. Run this list comprehension in your prompt:

		[x+y for x in [10,20,30] for y in [1,2,3]]

   Figure out what is going on here, and write a nested for loop that gives you the same result. Make sure what is going on makes sense to you!

[course notes]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_chap02.pdf

[this site]: http://www.secnetix.de/olli/Python/list_comprehensions.hawk
