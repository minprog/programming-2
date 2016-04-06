# Objects and their classes

Now, on to the paradigm of object-oriented programming! To get started, read up on the ideas and examples:

* Chapter 15: [Classes and objects](http://www.greenteapress.com/thinkpython/html/thinkpython016.html)
* Chapter 16: [Classes and Functions](http://www.greenteapress.com/thinkpython/html/thinkpython017.html)
* Chapter 17: [Classes and Methods](http://www.greenteapress.com/thinkpython/html/thinkpython018.html)
* Chapter 18: [Inheritance](http://www.greenteapress.com/thinkpython/html/thinkpython019.html)

## Questions about object-oriented programming

To make sure you understand some of the core ideas of object-oriented programming, here are some questions to answer. Discuss with your fellow students and staff if unsure how to answer.

1. What is the difference between a local variable and an object's attribute?

2. What method is called when the object is created?

3. If you have an object instance, `obj`, and you want to call its do `something()` method
   (assuming it has one), how would you do this in code?

## Understanding Objects

1. Write a class called `Address` that has two attributes: number and street
   name. Make sure you have an init method that initializes the object
   appropriately.

2. Consider the following code:
 
        class Clock:
            def __init__(self, time):
                self.time = time
            def print_time(self):
                time = '6:30'
                print self.time
        clock = Clock('5:30')
        clock.print_time()

    1. What does the code print out? If you aren't sure, create a Python file and run it.
    2. Is that what you expected? Why?

3. Consider the following code:

        class Clock:
            def __init__(self, time):
                self.time = time
            def print_time(self, time):
                print time
        clock = Clock('5:30')
        clock.print_time('10:30')

	1. What does the code print out? If you aren't sure, create a Python file and run it.
	2. What does this tell you about giving parameters the same name as object attributes?

4. Consider the following code:

        class Clock:
            def __init__(self, time):
                self.time = time
            def print_time(self):
                print self.time
        boston_clock = Clock('5:30')
        paris_clock = boston_clock
        paris_clock.time = '10:30'
        boston_clock.print_time()

	1. What does the code print out? If you aren't sure, create a Python file and run it.
    2. Why does it print what it does? (Are boston clock and paris clock different objects? Why or why not?)

## Implementing a data structure as a class

For this exercise, you will be coding a `Queue` class. Recall that, if you want to get something out
of a queue, you get the item that has been in there the longest.

Create a new file called `queue.py` to make your `Queue` class. In your `Queue` class, you will need three methods:

* `__init__`: to initialize your `Queue` (think: how will you store the queue's elements? You'll
  need to initialize an appropriate object attribute in this method)

* `insert`: inserts one element in your `Queue`

* `remove`: removes one element from your `Queue` and returns it. If the queue is empty, return a
  message that says it is empty.

When you're done, test your implementation "by hand". Your results should look like this:

    >> queue = Queue()
    >> queue.insert(5)
    >> queue.insert(6)
    >> queue.remove()
    5
    >> queue.insert(7)
    >> queue.remove()
    6
    >> queue.remove()
    7
    >> queue.remove()
    The queue is empty

Be sure to handle that last case correctly; when popping from an empty `Queue`, print a nice
message rather than throw an error!

## And a similar class

This problem builds on your work on the `Queue` class. Stacks are the opposite of queues: instead
of being *first-in­ first-out*, they use a *last-in-first-out* (LIFO) strategy.

Make a new file `stack.py` and implement a `Stack` class. It should be very similar
to your `Queue` implementation; the three methods your class will need will be
`__init__`, `push`, and `pop`. When you're done, you should test your
implementation. Your results should look like this:

    >> stack = Stack()
    >> stack.push(5)
    >> stack.push(6)
    >> stack.pop()
    6
    >> stack.push(7)
    >> stack.pop()
    7
    >> stack.pop()
    5
    >> stack.pop()
    The stack is empty
