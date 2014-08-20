# 3.0 Your First Class - Queue

This exercise, plus the remaining questions will be the start of our journey into object-oriented
programming; we suggest you do these questions before tackling this question.
For this exercise, you will be coding your very first class, a Queue class. Queues are a fundamental computer science
data structure. A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain
a specific order. When you want to get something off the end of a queue, you get the item that has been in there
the longest (this is known as ‘first-in-first-out’, or FIFO). You can read up on queues at Wikipedia if you’d like to
learn more.

Create a new file called queue.py to make your Queue class. In your Queue class, you will need three methods:
* \_\_init\_\_ : to initialize your Queue (think: how will you store the queue’s elements? You’ll need to initialize
an appropriate object attribute in this method)
* insert: inserts one element in your Queue
* remove: removes one element from your Queue and returns it. If the queue is empty, return a message that
says it is empty.

When you’re done, you should test your implementation. Your results should look like this:

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

Be sure to handle that last case correctly - when popping from an empty Queue, print a message rather than
throwing an error.

# 3.1 Your second Class - Stack
This problem builds on your work in Exercise 3.0. Stacks are the opposite of queues - instead of being ‘first-in­
first-out’, they use a ‘last-in-first-out’ (LIFO) strategy. Think of them like a pop-up stack of plates at a restaurant;
the first plate put in will be the last one pulled out and used. Again, check out Wikipedia for a more in-depth
explanation.

Make a new file stack.py and implement a Stack class. It should be very similar to your Queue implementation;
the three methods your class will need will be \_\_init\_\_, push, and pop.
When you’re done, you should test your implementation. Your results should look like this:

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
