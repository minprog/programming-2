# Scraping

In this assignment you will learn to use the Document Object Model (DOM) using Python via the
Pattern library. For the programming excercises in this homework, we provide both some scaffolding
and automated tests that are also used when grading the homework.

* The IMDB highest ranking TV-series exercise: [tvscraper.py]
* The test script for this exercise [test-tvscraper.py]

[tvscraper.py]: tvscraper.py
[test-tvscraper.py]: test-tvscraper.py

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

[output.csv]: output.csv
[test-tvscraper.py]: test-tvscraper.py

## Building `scraper.py`

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
