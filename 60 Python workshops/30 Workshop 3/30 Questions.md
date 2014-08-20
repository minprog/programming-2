## Intro to Object Oriented Programming
1. What is the difference between a local variable and an object’s attribute?
2. What method is called when the object is created?
3. If you have an object instance, obj, and you want to call its do something() method (assuming it has one),
how would you do this? (write the line of code you would use)

## Understanding Objects
1. Write a class called Address that has two attributes: number and street name. Make sure you have an
init method that initializes the object appropriately.
<textarea name="a[3-1-1]"></textarea>

2. Consider the following code:
 
		class Clock:
		    def __init__(self, time):
		        self.time = time
		    def print_time(self):
		        time = ’6:30’
		        print self.time
		clock = Clock(’5:30’)
		clock.print_time()

	(a) What does the code print out? If you aren’t sure, create a Python file and run it.
	<textarea name="a[3-2-1]"></textarea><br/>
	(b) Is that what you expected? Why?
	<textarea name="a[3-2-2]"></textarea>

3. Consider the following code:

		class Clock:
		    def __init__(self, time):
		        self.time = time
		    def print_time(self, time):
		        print time
		clock = Clock(’5:30’)
		clock.print_time(’10:30’)

	(a) What does the code print out? If you aren’t sure, create a Python file and run it.
	<textarea name="a[3-3-1]"></textarea><br/>
	(b) What does this tell you about giving parameters the same name as object attributes?
	<textarea name="a[3-3-2]"></textarea>

4. Consider the following code:

		class Clock:
		    def __init__(self, time):
		        self.time = time
		    def print_time(self):
		        print self.time
		boston_clock = Clock(’5:30’)
		paris_clock = boston_clock
		paris_clock.time = ’10:30’
		boston_clock.print_time()

	(a) What does the code print out? If you aren’t sure, create a Python file and run it.
	<textarea name="a[3-4-1]"></textarea><br/>
	(b) Why does it print what it does? (Are boston clock and paris clock different objects? Why or why
not?)
<textarea name="a[3-4-2]"></textarea>
