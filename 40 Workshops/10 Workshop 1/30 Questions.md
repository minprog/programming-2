# Questions

These exercises do not ask you to create a new Python program, but instead ask
you to read some code and predict the answer. Sometimes the questions are about
other things related to programming.

## Exercise 1.9 – Variable Names

The Python interpreter has strict rules for variable names. Which of the
following are legal Python names? If the name is not legal, state the reason.

|expression |legal?                             |
|-----------|-----------------------------------|
|`and`      |<input name="a[1-9-1]" type="text">|
|`_and`     |<input name="a[1-9-2]" type="text">|
|`var`      |<input name="a[1-9-3]" type="text">|
|`var1`     |<input name="a[1-9-4]" type="text">|
|`1var`     |<input name="a[1-9-5]" type="text">|
|`my-name`  |<input name="a[1-9-6]" type="text">|
|`your_name`|<input name="a[1-9-7]" type="text">|
|`COLOR`    |<input name="a[1-9-8]" type="text">|

## Exercise 1.10 – Types

It is important that we know the type of the values stored in a variable so that we can use the correct operators (as we have already seen!). Python automatically infers the type from the value you assign to the variable. Write down the type of the values stored in each of the variables below. Pay special attention to punctuation: values are not always the type they seem!

|variable       |type                                |
|---------------|------------------------------------|
|`a = False`    |<input name="a[1-10-1]" type="text">|
|`b = 3.7`      |<input name="a[1-10-2]" type="text">|
|`c = 'Alex'`   |<input name="a[1-10-3]" type="text">|
|`d = 7`        |<input name="a[1-10-4]" type="text">|
|`e = 'True'`   |<input name="a[1-10-5]" type="text">|
|`f = 17`       |<input name="a[1-10-6]" type="text">|
|`g = '17'`     |<input name="a[1-10-7]" type="text">|
|`h = True`     |<input name="a[1-10-8]" type="text">|
|`i = '3.14159'`|<input name="a[1-10-9]" type="text">|

To verify your answers, you can use the interactive Python shell, but first try to do the exercise without help.

	>>> x = 100
	>>> type(x)
	<type 'int'>
	>>>

## Exercise 1.14 – Understanding loops

For each of the following fragments of code, write what the output would be. Again, do this without running the code (although feel free to check yourself when you're done).

{: .language-python}
	num = 10
	while num > 3:
		print num
		num = num - 1

> <textarea name="a[1-14-1]"></textarea>

{: .language-python}
	divisor = 2
	for i in range(0, 10, 2):
		print i/divisor

> <textarea name="a[1-14-2]"></textarea>

{: .language-python}
	num = 10
	while True:
		if num < 7:
			break
		print num
		num -= 1

> <textarea name="a[1-14-3]"></textarea>

{: .language-python}
	count = 0
	for letter in 'Snow!':
		print 'Letter #', count, 'is', letter
		count += 1

> <textarea name="a[1-14-4]"></textarea>

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