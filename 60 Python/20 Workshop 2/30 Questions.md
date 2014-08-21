# List and string operations

String operators might be a little less intuitive than those on numbers. This
exercise will give you a chance to practice those. Given the following 
variables:

	look = 'Look at me!'
	now = ' NOW'

What are the values of the following expressions? Try to guess on your own
before using your interpreter (but feel free to use your interpreter once you 
get stuck).

|expression                           |value                               |
|-------------------------------------|------------------------------------|
|`look[:4]`                           |<input name="a[2-1-1]" type="text">|
|`look[-1]`                           |<input name="a[2-1-2]" type="text">|
|`look*2`                             |<input name="a[2-1-3]" type="text">|
|`look[:-1] + now + look[-1]`         |<input name="a[2-1-4]" type="text">|
|`now[1]`                             |<input name="a[2-1-5]" type="text">|
|`now[4]`                             |<input name="a[2-1-6]" type="text">|
|`look*2 + look[:-1] + now + look[-1]`|<input name="a[2-1-7]" type="text">|

For more on strings, see [the Python docs](http://docs.python.org/release/2.7.5/library/stdtypes.html#string-methods).

# List operations

Say we have this list:

	a_list = [3, 5, 6, 12]

For the following, write the line(s) of code that will emit the given output.
For each problem there may be more than one correct answer; just give one. 

More on lists: [the Python docs](http://docs.python.org/release/2.7.5/tutorial/datastructures.html).

1.	Output: `3`

	<textarea name="a[2-2-1]"></textarea>

2.	Output: `12`

	<textarea name="a[2-2-2]"></textarea>

3.	Output: `[5, 6, 12]`

	<textarea name="a[2-2-3]"></textarea>

4.	Output:

		3
		5
		6
		12

	<textarea name="a[2-2-4]"></textarea>

5.	Output: `[12, 6, 5, 3]`

	<textarea name="a[2-2-5]"></textarea>

6.	Output: `[9, 15, 18, 36]`

	<textarea name="a[2-2-6]"></textarea>

7.	Output: `[False, False, True, True]`

	<textarea name="a[2-2-7]"></textarea>

## Mutability

We've learned about many Python data structures (strings, lists, tuples,
dictionaries). For both "mutable" and "immutable", please give a short (5
words or fewer) definition, and then list what data structure(s) have that
characteristic.

Mutable:

<textarea name="a[2-3-1]"></textarea>

Immutable:

<textarea name="a[2-3-2]"></textarea>

## Finding Bugs

The following set of instructions were given to Ben Bitdiddle, and he produced
the code below. Find at least three bugs he made, and say how to fix them.

Instructions: Write a negate function that takes a number and returns the
negation of that number. Also write a large num function that takes a number,
and returns True if that number is bigger than 10000, and False otherwise.
Additionally, write some code to test your functions.

	def negate(num):
		return -num

	def large_num(num):
		res = (num > 10000)

	negate(b)
	neg_b = num
	print 'b:', b, 'neg_b:', neg_b

	big = large_num(b)
	print 'b is big:', big

Bugs:

1. <textarea name="a[2-4-1]"></textarea>

2. <textarea name="a[2-4-2]"></textarea>

3. <textarea name="a[2-4-3]"></textarea>

## A Mystery Program

Ben next turned in the following uncommented code (WTF?? WHY) to the
assistants. Help us figure out what it does!

	 1 print "Think of a number between 1 and 100, but don't tell me what you choose."
	 2 min_n = 1
	 3 max_n = 100
	 4 right_answer = False
	 5
	 6 while not right_answer:
	 7     mid_n = (max_n + min_n + 1)/2
	 8     answer = raw_input('Is it ' + str(mid_n) + '? ')
	 9     if answer[0] == 'y':
	10         right_answer = True
	11     elif answer.startswith('higher'):
	12         min_n = mid_n + 1
	13     elif answer.startswith('lower'):
	14         max_n = mid_n - 1
	15     else:
	16         print "Sorry, I don't understand your answer."
	17
	18 print 'Woohoo! I got it!'

1. The while loop exits when the variable right answer is True. What will
   cause right answer to be true?

   <textarea name="a[2-5-1]"></textarea>

2. How many times will the program print out 'Woohoo! I got it!'?

   <textarea name="a[2-5-2]"></textarea>

3. What are we using the variable answer for?

   <textarea name="a[2-5-3]"></textarea>

4. The program makes a guess in line 8. What user responses will be understood
   by the program after it makes its guess?

   <textarea name="a[2-5-4]"></textarea>

5. If the program gets the response 'higher', what does that tell it about its
   guess?

   <textarea name="a[2-5-5]"></textarea>

6. What are the variables min n, max n and mid n used for?

   <textarea name="a[2-5-6]"></textarea>

This is an example of binary search, a simple but important algorithm in
computer science. If you're curious, or confused, read the Wikipedia article
on binary search to find out more and get a good explanation of what's going
on here.
