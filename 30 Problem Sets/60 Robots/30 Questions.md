# Questions about object-oriented programming

To make sure you understand some of the core ideas of object-oriented programming, here are some questions to answer. Discuss with your fellow students and staff if unsure of an answer.

1. What is the difference between a local variable and an object's attribute?

2. What method is called when the object is created?

3. If you have an object instance, `obj`, and you want to call its do
`something()` method (assuming it has one), how would you do this in code?

## Understanding Objects

1. Write a class called `Address` that has two attributes: number and street
name. Make sure you have an init method that initializes the object
appropriately.

2. Consider the following code:
 
        class Clock:
            def __init__(self, time):
                self.time = time
            def print_time(self):
                time = ’6:30’
                print self.time
        clock = Clock(’5:30’)
        clock.print_time()

    1. What does the code print out? If you aren’t sure, create a Python file and run it.
    2. Is that what you expected? Why?

3. Consider the following code:

        class Clock:
            def __init__(self, time):
                self.time = time
            def print_time(self, time):
                print time
        clock = Clock(’5:30’)
        clock.print_time(’10:30’)

	1. What does the code print out? If you aren’t sure, create a Python file and run it.
	2. What does this tell you about giving parameters the same name as object attributes?

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

	1. What does the code print out? If you aren’t sure, create a Python file and run it.
    2. Why does it print what it does? (Are boston clock and paris clock different objects? Why or why not?)
