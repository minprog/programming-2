# Breakout

* Let's ensure that the Appliance is up to date by running `update50` from a Terminal before starting.

## Getting started

![videoplayer](http://cdn.cs50.net/2012/fall/shorts/pointers/pointers-720p.mp4)

![videoplayer](http://cdn.cs50.net/2012/fall/shorts/strings/strings-720p.mp4)

![videoplayer](http://cdn.cs50.net/2012/fall/shorts/cs50_library/cs50_library-720p.mp4)

* Your challenge for this problem set is to implement the Breakout.

  Now, Problem Set 3 was also a game, but its graphical user interface (GUI) wasn't exactly a GUI; it was more of a textual user interface, since we essentially simulated graphics with printf. Let's give Breakout an actual GUI by building atop the Stanford Portable Library (SPL), which is similar in spirit to the CS50 Library but includes an API (application programming interface) for GUI programming and more.

## SPL examples

* Execute

		cd ~/Dropbox
  
  and then

		wget http://cdn.cs50.net/2013/fall/lectures/5/m/src5m.zip
		unzip src5m.zip
		rm src5m.zip
		cd src5m

  to download, unzip, and navigate to some example programs.

  There's quite a few files in this map, as can be confirmed by typing

		ls

  revealing

		bounce.c  checkbox.c  cursor.c  Makefile  spl      text.c
		button.c  click.c     label.c   slider.c  spl.jar  window.c

  You can compile all of these files at once by simply typing

		make

  thanks to the included `Makefile`.

* Let's take a closer look at each of these programs. First up is `window`.

		./window

  Upon executing this program, you should be seeing a window such as this one:

  ![Empty SPL window](41.png)

  Open up `windows.c` with `gedit`. 

<iframe width="711" height="400" src="https://www.youtube.com/embed/IMOujDlGebQ" frameborder="0" allowfullscreen></iframe>

  How did we know how to call `newGWindow` like that? Well, there aren't man pages for SPL, but you can look at the relevant header file (`gwindow.h`). In fact, notice that inside of `src5m` is a subdirectory called `spl`. Inside of that is another subdirectory called `include`. If you take a look there, you'll find `gwindow.h`. Open it up with `gedit` and look around. Hm, a bit overwhelming. You might find it easier to look [here](http://cdn.cs50.net/2013/fall/lectures/5/m/src5m/spl/doc/gwindow.html), which contains the same information organised in a somewhat more friendly way. Click `newGWindow` under Functions, and you'll see its prototype:

		GWindow newGWindow(double width, double height);

  So that's how we knew!

* Take a look at a few other files, namely `cursor.c`, `bounce.c`, `button.c`, `checkbox.c`, `label.c`, `slider.c`, and `text.c`. The following two videos discuss the first two of these; no videos for the others!

<iframe width="711" height="400" src="http://www.youtube.com/embed/xsB0v8GtVMw" frameborder="0" allowfullscreen></iframe>

<iframe width="711" height="400" src="http://www.youtube.com/embed/8RMHJe1ZpKM" frameborder="0" allowfullscreen></iframe>

# Breaking out

* Now that we're accustomed to some of the features of SPL, let's get started on the problem set for this week. Perform the following command to grab the distribution code of this week. Ensure you're in `~/Dropbox`.

		wget http://cdn.cs50.net/2013/fall/psets/4/pset4/pset4.zip

  Then unzip `pset4.zip` and move yourself into the `pset4` directory. Perform `ls` while in this directory to ensure yourself the following files and folders are present:

		breakout.c   Makefile   spl   spl.jar

  You can actually compile and run `breakout` out of the box right away, which should give you an empty window when executed. To confirm as much, do so:

		make
		./breakout

  Let's see what you're supposed to make this week! Try out the staff implementation of `breakout` by typing

		~cs50/pset4/breakout

  which should open a window such as below:

  ![Starting configuration of breakout game](42.png)

  You can play the game by clicking somewhere in the window. Then use your cursor to move the bat around. (Don't worry if the game performs a bit laggy or choppy.)

* Let's make your implementation look more like that one. But, first, a tour!

* Open up `breakout.c` with `gedit` and take a moment to scroll through it to get a sense of what lies ahead. It's a bit reminiscent of the skeleton for Game of Fifteen, no? But definitely some new functions in there, most from SPL. Let's walk through it from top to bottom.

* Atop the file you'll see some familiar header files. We've also included `time.h` so that you have access to a "pseudorandom number generator" (PRNG), a function that can generate random (well, technically not-quite-random) numbers. We've also included some header files from SPL. Because those files are included in this problem set's distribution code (in `pset4/spl/include`), we've used, as is required by C, double quotes (`"`) around their filenames instead of the usual angled brackets (`<` and `>`) because they're not installed deep in the appliance itself.

* Next up are some constants, values that you don't need to change, but because the code we've written (and that you'll write) needs to know these values in a few places, we've factored them out as constants so that we or you could, theoretically, change them in one convenient location. By contrast, hard-coding the same number (pejoratively known as a "magic number") into your code in multiple places is considered bad practice, since you'd have to remember to change it, potentially, in all of those places.

* Below those constants are a bunch of prototypes for functions that are defined below `main`. More on each of those soon.

* Next up is our old friend, `main`. It looks like the first thing that main does is "seed" that so-called PRNG with the current time. (See `man srand48` and `man 2 time` if curious.) To seed a PRNG simply means to initialize it in such a way that the numbers it will eventually spit out will appear to be random. It's deliberate, then, that we're initializing the PRNG with the current time: time's always changing. Were we instead to initialize the PRNG with some hard-coded value, it'd always spit out the same sequence of "random" numbers.

* After that call to `srand48`, it looks like main calls `newGWindow`, passing in a desired `WIDTH` and `HEIGHT`. That function "instantiates" (i.e., creates) a new graphical window, returning some sort of reference thereto. (It's technically a pointer, but that detail, and the accompanying `*`, is, again, hidden from us by SPL.) That function's return value is apparently stored in a variable called `window` whose type is `GWindow`, which happens to be declared in a `gwindow.h` header file that you may have glimpsed earlier.

* Next, `main` calls `initBricks`, a function written partly by us (and, soon, mostly by you!) that instantiates a grid of bricks atop the game's window.

* Then `main` calls `initBall`, which instantiates the ball that will be used to play Breakout. Passed into that function is `window` so that the function knows where to "place" (i.e., draw) the ball. The function returns a `GOval` (graphical oval) whose width and height will simply be equal (ergo a circular ball).

* Called by main next is `initPaddle`, which instantiates the game's paddle; it returns a `GRect` (graphical rectangle).

* Then `main` calls `initScoreboard`, which instantiates the game's scoreboard, which is simply a `GLabel` (graphical label).

* Below all those function calls are a few definitions of variables, namely bricks, lives, and points. Below those is a loop, which is meant to iterate again and again so long as the user has lives left to live and bricks left to break. Of course, there's not much code in that loop now!

* Below the loop is a call to `waitForClick`, a function that does exactly that so that the window doesn't close until the user intends.

* Not too bad, right? Let's next take a closer look at those functions.

* In `initBricks`, you'll eventually write code that instantiates a grid of bricks in the window. Those constants we saw earlier, `ROWS` and `COLS`, represent that grid's dimensions. How to draw a grid of bricks on the screen? Well, odds are you'll want to employ a pair of for loops, one nested inside of the other. And within that innermost loop, you'll likely want to instantiate a GRect of some width and height (and color!) to represent a brick.

* In `initBall`, you'll eventually write code that instantiates a ball (that is, a circle, or really a `GOval`) and somehow center it in the window.

* In `initPaddle`, you'll eventually write code that instantiates a paddle (just a `GRect`) that's somehow centered in the bottom-middle of the game's window.

* Finally, in `initScoreboard`, you'll eventually write code that instantiates a scoreboard as, quite simply, a `GLabel` whose value is a number (well, technically, a `char*`, which we once knew as a string).

* Now, we've already implemented `updateScoreboard` for you. All that function does, given a `GWindow`, a `GLabel`, and an `int`, is convert the `int` to a string (okay, `char*`) using a function called `sprintf`, after which it sets the label to that value and then re-centers the label (in case the `int` has more digits than some previous `int`). Why did we allocate an array of size 12 for our representation of that `int` as a string? No worries if the reason's non-obvious, but give some though as to how wide the most positive (or most negative!) `int` might be. You're welcome to change this function, but you're not expected to.

* Last up is `detectCollision`, another function that we've written for you. (Phew!) This one's a bit more involved, so do spend some time reading through it. This function's purpose in life, given the ball as a `GOval`, is to determine whether that ball has collided with (i.e., is overlapping) some other object (well, `GObject`) in the game. (A `GRect`, `GOval`, or `GLabel` can also be thought of and treated as a `GObject`.) To do so, it cuts some corners (figuratively but also kind of literally) by checking whether any of the ball's "corners," as defined by the ball's "bounding box", per the below (wherein `x` and `y` represent coordinates, and `r` represents the ball's radius) are touching some other `GObject` (which might be a brick or a paddle or even something else).

## Let's go!

* Alright, if you're like me, odds are you'll find it easiest to implement Breakout via some baby steps, each of which will get you closer and closer to a great outcome. Rather than try to implement the whole game at once, allow me to suggest that you proceed as follows:

* Try out the staff's solution again (via `~cs50/pset4/breakout` from within your own ~/Dropbox/pset4 directory) to remind yourself how our implementation behaves. Yours doesn't need to be identical. In fact, all the better if you personalize yours. But playing with our implementation should help guide you toward yours.

* Implement `initPaddle`. Per the function's return value, your paddle should be implemented as a `GRect`. Odds are you'll first want to decide on a width and height for your paddle, perhaps declaring them both atop `breakout.c` with constants. Then calculate coordinates (`x` and `y`) for your paddle, keeping in mind that it should be initially aligned in the bottom-middle of your game's window. We leave it to you to decide exactly where. Odds are some arithmetic involving the window's width and height and the paddle's width and height will help you center it. Keep in mind that `x` and `y` refer to a `GRect`'s top-left corner, not its own middle. Your paddle's size and location doesn't need to match the staff's precisely, but it should be perfectly centered, near the window's bottom. You're welcome to choose a color for it too, for which `setColor` and `setFilled` might be of interest. Finally, instantiate your paddle with `newGRect`. (Take note of that function's prototype, which you can find [http://cdn.cs50.net/2013/fall/psets/4/pset4/pset4/spl/doc/gobjects.html](here).) Then return the `GRect` returned by `newGRect` (rather than `NULL`, which the distribution code returns only so that the program will compile without `initPaddle` fully implemented).

  Now, `initPaddle`'s purpose in life is only to instantiate and return a paddle (i.e., `GRect`). It shouldn't handle any of the paddle's movement. For that, turn your attention to the `TODO` up in `main`. Proceed to replace that `TODO` with some lines of code that respond to a user's mouse movements in such a way that the paddle follows the movements, but only along its (horizontal) x-axis. Look back at `cursor.c` for inspiration, but keep in mind that `cursor.c` allowed that circle to move along a (vertical) y-axis as well, which we don't want for Breakout, else the paddle could move anywhere (which might be cool but not exactly Breakout).

* Now turn your attention to the `TODO` in `initBricks`. Implement that function in such a way that it instantiates a grid of bricks (with `ROWS` rows and `COLS` columns), with each such brick implemented as a `GRect`. Drawing a `GRect` (or even a bunch of them) isn't all that different from drawing a `GOval` (or circle). Odds are, though, you'll want to instantiate them within a for loop that's within a for loop. (Think back to mario, perhaps!) Be sure to leave a bit of a gap between adjacent bricks, just like we did; exactly how many pixels is up to you. And we leave it to you to select your bricks' colors.

* Now implement `initBall`, whose purpose in life is to instantiate a ball in the window's center. (Another opportunity for a bit of arithmetic!) Per the function's prototype, be sure to return a `GOval`.

* Then, back in `main`, where there used to be a `TODO`, proceed to write some additional code (within that same while loop) that compels that ball to move. Here, too, take baby steps. Look to `bounce.c` first for ideas on how to make the ball bounce back and forth between your window's edges. (Not the ultimate goal, but it's a step toward it!) Then figure out how to make the ball bounce up and down instead of left and right. (Closer!) Then figure out how to make the ball move at an angle. Then, utilize `drand48` to make the ball's initial velocity random, at least along its (horizontal) x-axis. Note that, per its `man` page, `drand48` returns "nonnegative double-precision floating-point values uniformly distributed between `[0.0, 1.0)`." In other words, it returns a double between `0.0` (inclusive) and `1.0` (exclusive). If you want your velocity to be faster than that, simply add some constant to it and/or multiply it by some constant!

  Ultimately, be sure that the ball still bounces off edges, including the window's bottom for now.

  When ready, add some additional code to `main` (still somewhere inside of that while loop) that compels the ball to bounce off of the paddle if it collides with it on its way downward. Odds are you'll want to call that function we wrote, `detectCollision`, inside that loop in order to detect whether the ball's collided with something so that, if so, you can somehow handle such an event. Of course, the ball could collide with the paddle or with any one of those bricks. Keep in mind, then, that `detectCollision` could return any such `GObject`; it's left to you to determine what has been struck. Know, then, that if you store its return value, as with

		GObject object = detectCollision(window, ball);

  you can determine whether that object is your game's paddle, as with the below.

		if (object == paddle)
		{
		    // TODO
		}

  More generally, you can determine if that object is a `GRect` with:

		if (strcmp(getType(object), "GRect") == 0)
		{
		    // TODO
		}

  Once it comes time to add a `GLabel` to your game (for its scoreboard), you can similarly determine if that object is `GLabel`, in which case it might be a collision you want to ignore. (Unless you want your scoreboard to be something the ball can bounce off of. Ours isn't.)

		if (strcmp(getType(object), "GLabel") == 0)
		{
		    // TODO
		}

* Once you have the ball bouncing off the paddle (and window's edges), focus your attention again on that while loop in `main` and figure out how to detect if the ball's hit a brick and how to remove that brick from the grid if so. Odds are you'll find removeGWindow of interest, per http://cdn.cs50.net/2013/fall/lectures/5/m/src5m/spl/doc/gwindow.html. SPL's documentation incorrectly refers to that function as `remove`, but it's indeed `removeGWindow` you want, whose prototype, to be clear, is the below.

		void removeGWindow(GWindow gw, GObject gobj);

* Now decide how to determine whether the ball has zoomed past the paddle and struck the window's bottom edge, in which case the user should lose a life and gameplay should probably pause until the user clicks the mouse button, as in the staff's implementation. Odds are detecting this situation isn't all that different from the code you already wrote for bouncing; you just don't want to bounce off that bottom edge anymore!

* Lastly, implement `initScoreboard` in such a way that the function instantiates and positions a `GLabel` somewhere in your game's window. Then, enhance `main` in such a way that the text of that `GLabel` is updated with the user's score anytime the user breaks a brick. Indeed, be sure that your program keeps track of how many lives remain and how many bricks remain, the latter of which is inversely related to how many points you should give the user for each brick broken; our solution awards one point per brick, but you're welcome to offer different rewards. A user's game should end (i.e., the ball should stop moving) after a user runs out of lives or after all bricks are broken. We leave it to you to decide what to do in both cases, if anything more!

* Because this game expects a human to play, no `check50` for this one! Best to invite some friends to find bugs!

## Final steps

* When you are done with `breakout.c`, submit it by going over to the **Submit** tab. Be sure to compile and test one last time before you submit.

* All done!
