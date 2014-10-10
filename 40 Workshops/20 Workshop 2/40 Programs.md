# Plotting

Ooooh this is nice! Easy graphical output with Python. This exercise will learn
you how to integrate other people's functions into your own program. Pyplot is
a library of functions that make it easy to plot data.

Work through the [Pyplot tutorial] and create a file called `pyplot.py` to save
your tutorial tests. Put each example in a separate function!

[Pyplot tutorial]: http://matplotlib.org/users/pyplot_tutorial.html

# Data processing tutorial

First, download [population.csv](population.csv) (**download, not open in
Excel!**), containing a list of the population counts in the Netherlands over
the last 60 years.

You will need to read this file and plot its data. Have a look at it first,
it's quite small.

Next, open your Python Shell and try to read it into Python:

	>>> import csv
	>>> file = csv.reader(open("home/jharvard/Dropbox/YOUR\_FOLDER/population.csv"))
	>>> file.next()
	>>> ['country', 'country isocode', 'year', 'POP']

Cool! Apparently Python can read your file. This first line isn't so
interesting to our program. But it does tell us what data can be found where.

Did you notice that the line is output by Python as a **list**? That is very
convenient. It appears that `csv.reader` will read a line and convert it into
an array containing the data fields.

Now, let's go on:

	>>> file.next()
	>>> ['Netherlands', 'NLD', '1950', '10113.527']

Now, that's the *real* data. Line 2 and all other lines contain the data that
was promised.

Let's parse the data:

	>>> line = file.next()
	>>> line[0]
	'Netherlands'

So you can actually save the next line in a variable and use it as a list.
Column 0 always contains the string `'Netherlands'`. And column 1 always
contains `'NLD'`.

Column 2 and 3 are more interesting. They contain the year and population in
that year. But... they are strings. That's of no use in calculations. And
there's a decimal point in the population count!

## Printing the population list nicely

Your first assignment with this file is to print the data to the screen.
Create a file called `population.py` and define a function like this:

	def print_population_list(filename):
		'''
		Prints the population read from a CSV file, containing 
		years in column 2 and population / 1000 in column 3.

		@param filename: the filename to read the data from
		'''

It is called `print_...` so it may print something! It should have this
**exact** output:

	1950: 10113527
	1951: 10264311
	1952: 10381988
	...

... and so on for each line in the data set.

Put your test call right below the function definition:

	print_population_list('N:\population.csv')

## Reading the list into a dictionary

This data connects a population count to a year. So a **dictionary** is the
perfect data structure to put this data in.

Define a function that reads all lines and `return`s the data in a dictionary
object.

	def population_dict(filename):
		"""
		Reads the population from a CSV file, containing 
		years in column 2 and population / 1000 in column 3.

		@param filename: the filename to read the data from
		@return dictionary containing year -> population
		"""

Also, the year in the dictionary should be of a reasonable type. An integer is
ok, but a string is also fine. The population however, is interesting to do
calculations with, so we would like to have that as an integer.

Test the function with this call below your code:

	print population_dict('N:\population.csv')

## Plotting the population

Now that we can read the census data into a dictionary, we can do other stuff
with it.

Create a function that plots data from a dictionary in a graph. Give it a
reasonable name. The function should have an extra parameter that tells us
what the title of the plot should be. Pass this title to `pyplot`.

Of course, because nothing is ever *easy*, you can't feed `pyplot` a
dictionary. It wants lists of the same length: in this case, one containing
the year labels, and one containing the data. How can you extract these lists
from a dictionary? It's quite simple, look it up.

Again, put a test that calls your function in the file! It needs to read a
dictionary and save it, and then pass that dictionary to the plotting function
you just made.

## Calculating year-over-year growth

Now, we want some more statistics. Let's calculate the year-over-year growth
percentage.

Create a function that takes one dictonary as a parameter and returns a new
dictionary containing year-over-year growth rates. You already know how to
extract the population count list from the dictionary. You also know how to
calculate a growth rate from one year to the next. And you know how to save
each calculated rate into a new list.

You probably don't know yet how you can easily create a new dictionary from
the list you just calculated. Say we have created a list `growth_rates` and we
already had the list `years`, then:

	growth_rates = [0.2, 0.23, 0.209, 0.31, ...]
	years = [1950, 1951, 1952, 1953, ...]
	
	growth_rate_dict = dict(zip(years, growth_rates))

`zip` is actually a very cool function. It creates one list from two lists.
Each element of the new list is a tuple, containing one element from list 1
and one element from list 2. And then we put it in the `dict` function to
convert it to a dictionary. Nice!

Plot your new dictionary using the same function that you defined previously.

## Acknowledgements

Thanks to Mark Guzdial's Computational Freakonomics class for a reference to
the data we used here.

The Netherlands population data / PWT 7.1 Alan Heston, Robert Summers and
Bettina Aten, Penn World Table Version 7.1, Center for International
Comparisons of Production, Income and Prices at the University of
Pennsylvania, Nov 2012.


# Hacker edition: List comprehensions

List comprehensions follow naturally from set builder notation and lambda calculus. They are very cool and make your life a lot easier. Don't worry if you don't get them yet.

Read about list comprehensions on pages 34-35 of the 6.01 [course notes]; the Wikipedia article on them are good, and [this site] is concise and good.

Put these exercises in `comprehensions.py`.

1. Write a list comprehension that prints a list of the cubes of the numbers 1 through 10.

2. Write a list comprehension that prints out the possible results of two coin flips (one result would be 'ht'). (Hint - how many results should there be?)

3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string. 6
￼￼￼￼￼￼
4. Run this list comprehension in your prompt:

		[x+y for x in [10,20,30] for y in [1,2,3]]

   Figure out what is going on here, and write a nested for loop that gives you the same result. Make sure what is going on makes sense to you!

[course notes]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_chap02.pdf

[this site]: http://www.secnetix.de/olli/Python/list_comprehensions.hawk

And now, your challenge:

1. Write a function that takes in a list of elements of different types and uses a list comprehension to return all the elements of the list of type int. Note: The function isinstance will be of help here. Google "Python isinstance" and see if you can figure out what it does, or type help(isinstance) at the Python shell.

2. Write a list comprehension which solves the equation $$y = x^2 + 1$$. Your solution should print out a list of $$[x, y]$$ pairs; use the domain $$x in [−5, 5]$$ and the range $$y in [0, 10]$$.

3. Similarly, write a list comprehension that finds the integer solutions $$[x, y]$$ for a circle of radius 5.

4. Make your own list comprehension challenge! Write a comment of what you're trying to do in your code, then put the list comprehension below the comment.
