# Scraping

In this assignment you will learn to use the Document Object Model (DOM) using
Python via the Pattern library, in a few weeks you will also access the DOM
from Javascript. For the programming excercises in this homework, we provide
both some scaffolding and automated tests that are also used when grading the
homework.

* The IMDB highest ranking TV-series exercise: [tvscraper.py]
* The test script for this exercise [test-tvscraper.py]

[tvscraper.py]: distro/scraper/tvscraper.py
[test-tvscraper.py]: distro/scraper/test-tvscraper.py


== Academic Honesty

This course's philosophy on academic honesty is best stated as "be reasonable." The course recognizes that interactions with classmates and others can facilitate mastery of the course's material. However, there remains a line between enlisting the help of another and submitting the work of another. This policy characterizes both sides of that line.

The essence of all work that you submit to this course must be your own. Collaboration on problems is not permitted (unless explicitly stated otherwise) except to the extent that you may ask classmates and others for help so long as that help does not reduce to another doing your work for you. Generally speaking, when asking for help, you may show your code or writing to others, but you may not view theirs, so long as you and they respect this policy's other constraints. Collaboration on quizzes and tests is not permitted at all. Collaboration on the final project is permitted to the extent prescribed by its specification.

Below are rules of thumb that (inexhaustively) characterize acts that the course considers reasonable and not reasonable. If in doubt as to whether some act is reasonable, do not commit it until you solicit and receive approval in writing from your instructor. If a violation of this policy is suspected and confirmed, your instructor reserves the right to impose local sanctions on top of any disciplinary outcome that may include an unsatisfactory or failing grade for work submitted or for the course itself.

=== Reasonable

* Communicating with classmates about problems in English (or some other spoken language).
* Discussing the course's material with others in order to understand it better.
* Helping a classmate identify a bug in his or her code, such as by viewing, compiling, or running his or her code, even on your own computer.
* Incorporating snippets of code that you find online or elsewhere into your own code, provided that those snippets are not themselves solutions to assigned problems and that you cite the snippets' origins.
* Reviewing past years' quizzes, tests, and solutions thereto.
* Sending or showing code that you've written to someone, possibly a classmate, so that he or she might help you identify and fix a bug.
* Sharing snippets of your own solutions to problems online so that others might help you identify and fix a bug or other issue.
* Turning to the web or elsewhere for instruction beyond the course's own, for references, and for solutions to technical difficulties, but not for outright solutions to problems or your own final project.
* Whiteboarding solutions to problems with others using diagrams or pseudocode but not actual code.
* Working with (and even paying) a tutor to help you with the course, provided the tutor does not do your work for you.

=== Not Reasonable

* Accessing a solution to some problem prior to (re-)submitting your own.
* Asking a classmate to see his or her solution to a problem before (re-)submitting your own.
* Decompiling, deobfuscating, or disassembling the staff's solutions to problems.
* Failing to cite (as with comments) the origins of code, writing, or techniques that you discover outside of the course's own lessons and integrate into your own work, even while respecting this policy's other constraints.
* Giving or showing to a classmate a solution to a problem when it is he or she, and not you, who is struggling to solve it.
* Looking at another individual's work during a quiz or test.
* Paying or offering to pay an individual for work that you may submit as (part of) your own.
* Providing or making available solutions to problems to individuals who might take this course in the future.
* Searching for, soliciting, or viewing a quiz's questions or answers prior to taking the quiz.
* Searching for or soliciting outright solutions to problems online or elsewhere.
* Splitting a problem's workload with another individual and combining your work (unless explicitly authorized by the problem itself).
* Submitting (after possibly modifying) the work of another individual beyond allowed snippets.
* Submitting the same or similar work to this course that you have submitted or will submit to another.
* Using resources during a quiz beyond those explicitly allowed in the quiz's instructions.
* Viewing another's solution to a problem and basing your own solution on it.

## DOM scraping and traversal

To scrape data, we will be using Pattern, a Python web mining module. Its
description is as follows:

> Pattern is a web mining module for the Python programming language. It bundles
> tools for data mining (Google + Twitter + Wikipedia API, web spider, HTML DOM
> parser), natural language processing (tagger/chunker, n­gram search, sentiment
> analysis, WordNet), machine learning (vector space model, k­means clustering,
> Naive Bayes + k­NN + SVM classifiers) and network analysis (graph centrality
> and visualization). It is well documented and bundled with 30+ examples and
> 350+ unit tests.

Instructions:

1. We assume Python and pattern are installed (see [preparations] if this is not
the case).

2. We will be looking at IMDB TV Series and getting data off this website. To
get started, you should look at the `examples` folder within `patterns­2.5`
Under `01-web` folder, look at example `07-dom.py`. If you have `pattern2.6`
the example is in directory `01-web` in the file `12-dom.py`.

The documentation on the website is also useful.

3. To get you started we have provided you with a script [tvscraper.py] that
loads the correct IMDB address, makes a local backup of it (`tvseries.html`)
and outputs a CSV file (`tvseries.csv`) that will contain only a header until
you complete the implementation of the functions `extract_tvseries(dom)` and
`save_csv(f, tvseries)`.

4. To help you validate your script we provide both an example output CSV
file [output.csv] and a test script [test-tvscraper.py]. To use the latter you
must first run the `tvscraper.py` script (with the command
`python tvscraper.py`). This will copy the IMDB webpage to the local directory
and save a CSV file. After you get these files run `test-tvscraper.py` from
the same directory. If your implementation of the missing functions is
correct, you will see no ERROR of FAIL messages.

5. When you hand this exercise in be sure to submit: your `tvscraper.py`,
`tvseries.html` and `tvseries.csv`. This will allow us to verify that your
output CSV file is correct and that the script actually works given the HTML
from IMDB.

6. It could be that there are missing data (for instance the runtime), insert
   an appropriate value when something is missing.

[output.csv]: distro/scraper/output.csv
[test-tvscraper.py]: distro/scraper/test-tvscraper.py
[preparations]: http://data.mprog.nl/homework/preparations

### Building `scraper.py`

This is the introductory exercise to Pattern. We will try to guide you along as
much as possible, but you should read up on documentation and get used to doing
that. It's a really useful skill and a big part of programming is
self-­learning!

This is also just a skeleton so you actually don't have to use this at all. As
long as your code runs at the end of the day and produces the write results in
a CSV file, we're happy.

Print is probably going to be your best friend for debugging so print often
especially if something goes wrong.

This is taken from the documentation, which you should learn to read!

	The DOM object is a tree of Element and Text objects. All objects inherit
	from Node, DOM also inherits from Element.

	Node.type => NODE, TEXT, COMMENT, ELEMENT, DOM
	Node.parent => Parent Node object
	Node.children => List of child Node objects
	Node.next => Next Node in Node.parent.children
	Node.previous => Previous Node in Node.parent.children

	DOM.head => Element with tag name "head"
	DOM.body => Element with tag name "body"

	Element.tag => Element tag name, e.g. "body"
	Element.attributes => Dictionary of tag attribute, e.g. {"class": "header"}
	Element.content => Element HTML content as a string.
	Element.source => Element tag + content

	Element.get_element_by_id(value)
	Element.get_elements_by_tagname(value)
	Element.get_elements_by_classname(value)
	Element.get_elements_by_attribute(name=value)

	You can also use short aliases: by_id(), by_tag(), by_class(), by_attribute()
	The tag name passed to Element.by_tag()
	can include a class ("div.message") or an id ("div#header").
