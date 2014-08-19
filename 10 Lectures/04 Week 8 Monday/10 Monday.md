Lecture notes by Andrew Sellergren. [Watch the video.](http://cs50.tv/2013/fall/lectures/8/m/)

## Announcements and Demos

Problem Set 5 is now over, but the photo contest is not! Submit the link to
your photos by noon on Monday 11/4 for a chance to win a Leap Motion!

We offer a number of CS50 Seminars on a wide variety of topics to help you
gear up for your Final Project. Register here and check out past seminars
here. On the roster so far for this year are:

* Amazing Web Apps with Ruby on Rails
* Computational Linguistics
* Introduction to iOS
* JavaScript for Web Apps
* Leap Motion SDK
* meteor.js: JavaScript on the back end
* Node.js
* Sleek Android Design
* Web Security: Active Defense

Thanks to the folks at Leap Motion, we have ~30 devices available for those
who would like to develop their Final Project with one!

Short on Final Project ideas? Check out [projects.cs50.net](http://projects.cs50.net).

## From Last Time

### Linked Lists

We introduced linked lists as a data structure with dynamic size. One
tradeoff for this is that a linked list requires more memory than an array of
equal size. The extra memory is necessary to store the pointers within each
node. Another tradeoff is that search in a linked list runs in $$O(n)$$ even
if it’s sorted; in the worse case, we have to traverse the whole list because
we don’t have random access as we do in an array.

Recall our implementation of a linked list node:

	typedef struct node
	{
	    int n;
	    struct node* next;
	}
	node;

We must declare `next` as a `struct node*` because `node` is not yet fully defined.

### Hash Tables

We also discussed hash tables, which associate keys with values. The keys are
determined by taking a deterministic hash of the values using a hash
function. In our first example, this hash function simply took the first
letter of the name that we wanted to store, 0 for Alice, 1 for Bob, and so
on. In code, this might look like:

	int hash(char* s)
	{
	    return s[0] - 'A';
	}

This function is a little buggy, of course, because we’re not checking if s
is `NULL` and we’re not accounting for lowercase strings. But you get the
idea.

Hash tables inevitably have collisions in which two values have the same
hash. Linear probing was the first approach we looked at for handling
collisions. More compelling, however, was the second approach in which our
hash table consisted of pointers to linked lists. If a second value needed to
be inserted at a key, we simply add it to the beginning of the linked list.
By inserting at the beginning of the list, we maintain $$O(1)$$ insertion
time.

### Tries

The final data structure we examined was a trie. Both insertion time and
search time for a trie are $$O(k)$$, where $$k$$ is the length of the word
being inserted or searched for. But $$k$$ is really a constant since words
have a finite length, so insertion time and search time are actually $$O(1)$$.

A trie is a tree structure consisting of arrays of arrays. Each index in each
array stores a pointer to another array. Considering how many arrays we’re
actually storing, then, the tradeoff for a trie implementation is clearly the
memory it requires. Yet again, we see that there is a tradeoff between memory
and running time, between space and speed.

## Stacks

We’ve already seen that a program’s memory is called the stack because of the
way in which function frames are layered on top of each other. More
generally, a stack is a data structure that has its own advantages and
disadvantages compared to arrays, linked lists, hash tables, and tries.

We interact with stacks using only two basic operations: push and pop. To add
data to the stack, we push it onto the top of the stack. To retrieve data
from the stack, we pop it off the top of the stack. As a result, a stack
exhibits last in first out (LIFO) storage. The only data that we can retrieve
from the stack is the last data we added to it.

In what contexts might LIFO storage be useful? Clearly it’s useful for
organizing a program’s memory. As we’ll see soon, it’s also useful for
validating the tree structure of a web page’s HTML.

We might implement a stack like so:

	typedef struct
	{
	    int trays[CAPACITY];
	    int size;
	}
	stack;

It’s convenient to think of a stack like the stack of trays in the dining
halls. In the code above, `CAPACITY` is a constant defining the maximum number
of such trays that a stack can contain. Another integer named size stores the
number of trays currently in the stack.

Let’s say `CAPACITY` is 3. Initially, trays contains nothing but garbage
values and `size` is 0. Let’s say we push the number 9 onto the stack. Now
`size` becomes 1 and the 0th index of trays is set to 9. Next, we push 17
onto the stack, `size` becomes 2 and the 1st index of trays is set to 17.
Finally, we push 22 onto the stack, `size` becomes 3 and the 2nd index of
trays is set to 22. What happens when we try to push 27 onto the stack? We
can’t add it to the stack because we have filled all available indices in
trays. If our push function returned a Boolean, we would want it to return
false in this case.

One way to implement a stack with dynamic size would be to declare `trays` as
a pointer and `malloc` it at runtime. Another way would be to declare `trays`
as a pointer to a linked list.

## Queues

If you’re familiar with the lines that form outside the Apple store when a
new iPhone is released, then you’re familiar with queues. We also interact
with queues using two basic operations: enqueue and dequeue. Whereas stacks
exhibit LIFO storage, however, queues exhibit FIFO, i.e. first in first out,
storage. Imagine how upset the people outside the Apple store would be if the
line were implemented as a stack instead of a queue!

We can implement a queue using a struct:

	typedef struct
	{
	    int numbers[CAPACITY];
	    int front;
	    int size;
	}
	queue;

Note that our queue type is very similar to our `stack` type. Why do we need
the extra `int` for `queue`? `front` keeps track of the index of the next
value to be dequeued. If we add 9, 17, and 22 as we did to the stack and then
remove 9, we need to know that 17 should be the next value dequeued. `front`
is incremented whenever a value is dequeued, at least until we reach
`CAPACITY`.

What happens when we have one value in the last index of `numbers` and we
want to enqueue another number? We can use an operator called modulus (`%`)
to wrap around to index 0 of `numbers`. Our one value is at index 2, so if we
insert at 3 modulo `CAPACITY`, we’ll be inserting at index 0.

Using this approach, insertion into a queue runs in constant time.

## Trees

A trie is actually a specific type of a data structure called a *tree*:

![A tree.](tree.png)

A tree consists of 0 or more nodes. If there is at least one node, it is
called the *root*. Each node can have 0 or more *children*. A node with 0
children is called a *leaf*.

The diagram above shows a tree that has varying numbers of children for each
node. But if we are a little more strict in how many children a node can
have, we create a structure that’s easily searchable. Consider a binary tree,
in which a node can have at most two children. We could define this in code
like so:

	typedef struct node
	{
	    int n;
	    struct node* left;
	    struct node* right;
	}
	node;

### Binary Search Trees

A *binary search tree* is a special type of binary tree. What’s interesting
about a binary search tree is that a node’s left child is less than it and a
node’s right child is greater than it. Searching a tree like this is trivial
then: if the current node is less than the value we’re looking for, then we
move to the right child; if the current node is greater than the value we’re
looking for, then we move to the left child. An implementation of search
might look like this:

	bool search(int n, node* tree)
	{
	    if (tree == NULL)
	    {
	        return false;
	    }
	    else if (n < tree->n)
	    {
	        return search(n, tree->left);
	    }
	    else if (n > tree->n)
	    {
	        return search(n, tree->right);
	    }
	    else
	    {
	        return true;
	    }
	}

Remember that the `->` operator means to access and dereference a field
within a struct.

Note that both the first if condition and the final else condition in the
above are base cases. It’s not necessary to place them both at the top of our
logic.

## Teaser

Soon we’ll start working in HTML, a markup language that allows you to
specify what a web page should look like, and JavaScript, a programming
language that allows you to execute logic within a browser. Our first web
page will be implemented like so:

	<!DOCTYPE html>
	
	<html>
	    <head>
	        <title>hello, world</title>
	    </head>
	    <body>
	        hello, world
	    </body>
	</html>

If you get really clever, you may be able to implement a page like [Rob’s](http://cs.harvard.edu/rob/) or even [Hamster Dance](http://www.hamsterdance.org/hamsterdance/).
