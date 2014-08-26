# Mispellings

* 20-hour students are allowed two weeks to finish this problem set, but you must show the progress you've made during the first week by uploading your work-in-progress to our servers no later than 15:00 on Friday.

* 40-hour students are allowed one week to finish this problem set, but you must show the progress you've made during the first half of the week by uploading your work-in-progress to our servers no later than 15:00 on Tuesday.

## Getting started

![videoplayer](http://cdn.cs50.net/2012/fall/shorts/hash_tables/hash_tables-720p.mp4)

* This problem set comes with some distribution code that you'll need to download before getting started. Go ahead and execute

		cd ~/Desktop

  in order to navigate to your `~/Desktop` directory. Then execute

		wget http://cdn.cs50.net/2013/fall/psets/6/pset6/pset6.zip
		unzip pset6.zip
		rm -f pset6.zip

  Now dive into that pset6 directory by executing the below.

		cd pset6

  Now execute

		ls

  and you should see that the directory contains the below.

		dictionary.c  dictionary.h  Makefile  questions.txt  speller.c

  Interesting! Let's get started.

* Theoretically, on input of size n, an algorithm with a running time of n is asymptotically equivalent, in terms of O, to an algorithm with a running time of 2n. In the real world, though, the fact of the matter is that the latter feels twice as slow as the former.

  The challenge ahead of you is to implement the fastest spell-checker you can! By "fastest," though, we're talking actual, real-world, noticeable seconds—none of that asymptotic stuff this time.

  In `speller.c`, we've put together a program that's designed to spell-check a file after loading a dictionary of words from disk into memory. Unfortunately, we didn't quite get around to implementing the loading part. Or the checking part. Both (and a bit more) we leave to you!

  Before we walk you through `speller.c`, go ahead and open up `dictionary.h` with gedit. Declared in that file are four functions; take note of what each should do. Now open up `dictionary.c`. Notice that we've implemented those four functions, but only barely, just enough for this code to compile. Your job for this problem set is to re-implement those functions as cleverly as possible so that this spell-checker works as advertised. And fast!

  Let's get you started.

* Recall that `make` automates compilation of your code so that you don't have to execute `clang` manually along with a whole bunch of switches. However, as your programs grow in size, `make` won't be able to infer from context anymore how to compile your code; you'll need to start telling make how to compile your program, particularly when they involve multiple source (i.e., `.c`) files, as in the case of this problem set. And so we'll utilize a `Makefile`, a configuration file that tells make exactly what to do. Open up `Makefile` with gedit, and let's take a tour of its lines.

  The line below defines a variable called `CC` that specifies that `make` should use `clang` for compiling.

		CC = clang
  
  The line below defines a variable called `CFLAGS` that specifies, in turn, that clang should use some flags, most of which should look familiar.

		CFLAGS = -ggdb3 -O0 -Qunused-arguments -std=c99 -Wall -Werror

  The line below defines a variable called EXE, the value of which will be our program's name.

		EXE = speller
  
  The line below defines a variable called `HDRS`, the value of which is a space-separated list of header files used by speller.

		HDRS = dictionary.h

  The line below defines a variable called `LIBS`, the value of which is should be a space-separated list of libraries, each of which should be prefixed with `-l`. (Recall our use of `-lcs50` earlier this term.) Odds are you won't need to enumerate any libraries for this problem set, but we've included the variable just in case.

		LIBS =

  The line below defines a variable called `SRCS`, the value of which is a space-separated list of C files that will collectively implement speller.

		SRCS = speller.c dictionary.c

  The line below defines a variable called `OBJS`, the value of which is identical to that of `SRCS`, except that each file's extension is not `.c` but `.o`.

		OBJS = $(SRCS:.c=.o)
  
  The lines below define a "target" using these variables that tells make how to compile speller.

		$(EXE): $(OBJS) Makefile
		    $(CC) $(CFLAGS) -o $@ $(OBJS) $(LIBS)
  
  The line below specifies that our `.o` files all "depend on" `dictionary.h` and `Makefile` so that changes to either induce recompilation of the former when you run `make`.

		$(OBJS): $(HDRS) Makefile
  
  Finally, the lines below define another target for cleaning up this problem set's directory.

		clean:
		    rm -f core $(EXE) *.o

  Know that you're welcome to modify this `Makefile` as you see fit. In fact, you should if you create any `.c` or `.h` files of your own. But be sure not to change any tabs (i.e., `\t`) to spaces, since `make` expects the former to be present below each target. To be safe, uncheck Use Spaces under Tab Width at the bottom of gedit's window before modifying `Makefile`.

  The net effect of all these lines is that you can compile speller with a single command, even though it comprises quite a few files:

		make speller

  Even better, you can also just execute:

		make

  And if you ever want to delete `speller` plus any `core` or `.o` files, you can do so with a single command:

		make clean

  In general, though, anytime you want to compile your code for this problem set, it should suffice to run:

		make

* Okay, next open up `speller.c` with gedit and spend some time looking over the code and comments therein. You won't need to change anything in this file, but you should understand it nonetheless. Notice how, by way of `getrusage`, we'll be "benchmarking" (i.e., timing the execution of) your implementations of check, load, size, and unload. Also notice how we go about passing check, word by word, the contents of some file to be spell-checked. Ultimately, we report each misspelling in that file along with a bunch of statistics.

  Notice, incidentally, that we have defined the usage of speller to be

		Usage: speller [dictionary] text

  where dictionary is assumed to be a file containing a list of lowercase words, one per line, and text is a file to be spell-checked. As the brackets suggest, provision of dictionary is optional; if this argument is omitted, speller will use `/home/cs50/pset6/dictionaries/large` by default. In other words, running

		./speller text

  will be equivalent to running

		./speller ~cs50/pset6/dictionaries/large text

  where text is the file you wish to spell-check. Suffice it to say, the former is easier to type! (Of course, `speller` will not be able to load any dictionaries until you implement load in `dictionary.c`! Until then, you'll see `Could not load.`)

  Within the default dictionary, mind you, are 143,091 words, all of which must be loaded into memory! In fact, take a peek at that file to get a sense of its structure and size, as with gedit. Notice that every word in that file appears in lowercase (even, for simplicity, proper nouns and acronyms). From top to bottom, the file is sorted lexicographically, with only one word per line (each of which ends with `\n`). No word is longer than 45 characters, and no word appears more than once. During development, you may find it helpful to provide `speller` with a dictionary of your own that contains far fewer words, lest you struggle to debug an otherwise enormous structure in memory. In `/home/cs50/pset6/dictionaries/small` is one such dictionary. To use it, execute

		./speller ~cs50/pset6/dictionaries/small text

  where text is the file you wish to spell-check. Don't move on until you're sure you understand how speller itself works!

* Odds are, you didn't spend enough time looking over `speller.c`. Go back one square and walk yourself through it again!

* Okay, technically that last problem induced an infinite loop. But we'll assume you broke out of it. Open up `questions.txt` with gedit and answer each of the following questions in one or more sentences.

  1. What is pneumonoultramicroscopicsilicovolcanoconiosis?

  2. According to its `man` page, what does `getrusage` do?

  3. Per that same `man` page, how many members are in a variable of type `struct rusage`?

  4. Why do you think we pass before and after by reference (instead of by value) to calculate, even though we're not changing their contents?

  5. Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's for loop works.

  6. Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

  7. Why do you think we declared the parameters for check and load as const?

* So that you can test your implementation of `speller`, we've also provided you with a whole bunch of texts, among them the script from Austin Powers: International Man of Mystery, a sound bite from Ralph Wiggum, three million bytes from Tolstoy, some excerpts from Machiavelli and Shakespeare, the entirety of the King James V Bible, and more. So that you know what to expect, open and skim each of those files, as with gedit. For instance, to open `austinpowers.txt`, open a terminal window and execute the below.

		gedit ~cs50/pset6/texts/austinpowers.txt
  
  Alternatively, launch gedit, select **File > Open...**, click File System at left, double-click home at right, double-click cs50 at right, double-click pset6 at right, double-click texts at right, then double-click austinpowers.txt at right. (If you get lost, simply start these steps over!)

  Now, as you should know from having read over `speller.c` carefully, the output of speller, if executed with, say,

		./speller ~cs50/pset6/texts/austinpowers.txt
  
  will eventually resemble the below. For now, try executing the staff's solution (using the default dictionary) with the below.

		~cs50/pset6/speller ~cs50/pset6/texts/austinpowers.txt
  
  Below's some of the output you'll see. For amusement's sake, we've excerpted some of our favorite "misspellings." And lest we spoil the fun, we've omitted our own statistics for now.

		MISSPELLED WORDS
		
		[...]
		Bigglesworth
		[...]
		Fembots
		[...]
		Virtucon
		[...]
		friggin'
		[...]
		shagged
		[...]
		trippy
		[...]
		
		WORDS MISSPELLED:
		WORDS IN DICTIONARY:
		WORDS IN TEXT:
		TIME IN load:
		TIME IN check:
		TIME IN size:
		TIME IN unload:
		TIME IN TOTAL:
  
  `TIME IN load` represents the number of seconds that speller spends executing your implementation of load. `TIME IN check` represents the number of seconds that speller spends, in total, executing your implementation of check. `TIME IN size` represents the number of seconds that speller spends executing your implementation of size. `TIME IN unload` represents the number of seconds that speller spends executing your implementation of unload. `TIME IN TOTAL` is the sum of those four measurements.

  Incidentally, to be clear, by "misspelled" we mean that some word is not in the dictionary provided. "Fembots" might very well be in some other (swinging) dictionary.

# Rules

* Alright, the challenge ahead of you is to implement load, check, size, and unload as efficiently as possible, in such a way that TIME IN load, TIME IN check, TIME IN size, and TIME IN unload are all minimized. To be sure, it's not obvious what it even means to be minimized, inasmuch as these benchmarks will certainly vary as you feed speller different values for dictionary and for text. But therein lies the challenge, if not the fun, of this problem set. This problem set is your chance to design. Although we invite you to minimize space, your ultimate enemy is time. But before you dive in, some specifications from us.

  A. You may not alter `speller.c`.

  B. You may alter `dictionary.c` (and, in fact, must in order to complete the implementations of load, check, size, and unload), but you may not alter the declarations of load, check, size, or unload.

  C. You may alter `dictionary.h`, but you may not alter the declarations of load, check, size, or unload.

  D. You may alter `Makefile`.

  E. You may add functions to `dictionary.c` or to files of your own creation so long as all of your code compiles via `make`.

  F. Your implementation of check must be case-insensitive. In other words, if foo is in dictionary, then check should return true given any capitalization thereof; none of foo, foO, fOo, fOO, fOO, Foo, FoO, FOo, and FOO should be considered misspelled.

  G. Capitalization aside, your implementation of check should only return true for words actually in dictionary. Beware hard-coding common words (e.g., the), lest we pass your implementation a dictionary without those same words. Moreover, the only possessives allowed are those actually in dictionary. In other words, even if foo is in dictionary, check should return false given foo's if foo's is not also in dictionary.

  H. You may assume that check will only be passed strings with alphabetical characters and/or apostrophes.

  I. You may assume that any dictionary passed to your program will be structured exactly like ours, lexicographically sorted from top to bottom with one word per line, each of which ends with `\n`. You may also assume that dictionary will contain at least one word, that no word will be longer than `LENGTH` (a constant defined in `dictionary.h`) characters, that no word will appear more than once, and that each word will contain only lowercase alphabetical characters and possibly apostrophes.

  J. Your spell-checker may only take text and, optionally, dictionary as input. Although you might be inclined (particularly if among those more comfortable) to "pre-process" our default dictionary in order to derive an "ideal hash function" for it, you may not save the output of any such pre-processing to disk in order to load it back into memory on subsequent runs of your spell-checker in order to gain an advantage.

  K. You may research hash functions in books or on the Web, so long as you cite the origin of any hash function you integrate into your own code.
  
  L. You must implement the **hash table** data structure. **Do not implement TRIE, or an amalgam of the two data structures.**

  Alright, ready to go?

# Implementation

* Implement `load`.

<iframe width="711" height="400" src="http://www.youtube.com/embed/E_1D17P-bM0" frameborder="0" allowfullscreen></iframe>

* Implement `check`.

<iframe width="711" height="400" src="http://www.youtube.com/embed/r7CVY6O-XJw" frameborder="0" allowfullscreen></iframe>

* Implement `size`.

<iframe width="711" height="400" src="http://www.youtube.com/embed/lO8k5CjLk4U" frameborder="0" allowfullscreen></iframe>

* Implement `unload`.

<iframe width="711" height="400" src="http://www.youtube.com/embed/VodrNEvdBBc" frameborder="0" allowfullscreen></iframe>

  With regards to unload, make sure that you free any and all memory you allocated in `load`. Recall that `valgrind` is your newest best friend. Know that valgrind watches for leaks while your program is actually running, so be sure to provide command-line arguments if you want valgrind to analyze speller while you use a particular dictionary and/or text, as in the below.

		valgrind --leak-check=full ./speller ~cs50/pset6/texts/austinpowers.txt

  If you run valgrind without specifying a text for speller, your implementations of load and unload won't actually get called (and thus analyzed).
   
* How to check whether your program is outting the right misspelled words? Well, you're welcome to consult the "answer keys" in ~cs50/pset6/keys, as with the below.

		gedit ~cs50/pset6/keys/austinpowers.txt
  
  Alternatively, you could run your program on some text in one window, as with the below.

		./speller ~cs50/pset6/texts/austinpowers.txt
  
  And you can then run the staff's solution on the same text in another window, as with the below.

		~cs50/pset6/speller ~cs50/pset6/texts/austinpowers.txt
  
  And you could then compare the windows visually side by side. That could get tedious quickly, though. So you might instead want to "redirect" your program's output to a file (just like you may have done with generate in Problem Set 3), as with the below.

		./speller ~cs50/pset6/texts/austinpowers.txt > student.txt
		~cs50/pset6/speller ~cs50/pset6/texts/austinpowers.txt > staff.txt
  
  You can then compare both files side by side in the same window with a program like diff, as with the below.

		diff -y student.txt staff.txt
  
  Alternatively, to save time, you could just compare your program's output (assuming you redirected it to, e.g., `student.txt`) against one of the answer keys without running the staff's solution, as with the below.

		diff -y student.txt ~cs50/pset6/keys/austinpowers.txt
  
  If your program's output matches the staff's, diff will output two columns that should be identical except for, perhaps, the running times at the bottom. If the columns differ, though, you'll see a > or | where they differ. For instance, if you see

		MISSPELLED WORDS                                                MISSPELLED WORDS
		
		FOTTAGE                                                         FOTTAGE
		INT                                                             INT
		                                                              > EVIL'S
		s                                                               s
		                                                              > EVIL'S
		Farbissina                                                      Farbissina

  that means your program (whose output is on the left) does not think that EVIL's is misspelled, even though the staff's output (on the right) does, as is implied by the absence of EVIL's in the lefthand column and the presence of EVIL's in the righthand column.

  To test your code less manually (though still not exhaustively), you may also execute the below:

		check50 2013.pset6.speller dictionary.c dictionary.h Makefile
  
  Note that `check50` does not check for memory leaks, so be sure to run valgrind as `prescribed` as well.
  
* How to assess just how fast (and correct) your code is? Well, as always, feel free to play with the staff's solution, as with the below, and compare its numbers against yours.

		~cs50/pset6/speller ~cs50/pset6/texts/austinpowers.txt
  
* Congrats! At this point, your speller-checker is presumably complete (and fast!), so it's time for a debriefing. In `questions.txt`, answer each of the following questions in a short paragraph.

  8. What data structure(s) did you use to implement your spell-checker? Be sure not to leave your answer at just "hash table," "trie," or the like. Expound on what's inside each of your "nodes."

  9. How slow was your code the first time you got it working correctly?

  10. What kinds of changes, if any, did you make to your code over the course of the week in order to improve its performance?

  11. Do you feel that your code has any bottlenecks that you were not able to chip away at?

## Final steps

* You are required to upload your current progress on `dictionary.c`, `dictionary.h`, and `Makefile`, along with `progress.txt` describing what you've already completed and what still remains to be done. Make sure your current working version of the spellchecker compiles.
