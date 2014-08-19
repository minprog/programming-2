Lecture notes by Andrew Sellergren. [Watch the video.](http://cs50.tv/2013/fall/lectures/8/w/)

## Announcements and Demos

Problem Set 6 is one of the more challenging problem sets we will complete
this semester, so be sure to leave yourself plenty of time to work through
it! If you’re up for it, see how efficient your implementation is compared to
your classmates' on The Big Board.

Pre-Proposal for the Final Project is due Monday! It’s really just a casual,
thought-provoking conversation you should have with your TF.

Check out The CS50 Store to memorialize your time in the course! If you’re
interested in submitting your own design, be sure to follow the specs
outlined at cs50.net/design and listed here:

* PNG
* 200+ DPI
* 4000 x 4000 pixels
* 10 MB

## The Internet

### HTTP

How does the internet actually work? When you type `facebook.com` into your
browser (Chrome, Internet Explorer, Firefox, etc.), the browser makes an HTTP
request. HTTP, which stands for hypertext transfer protocol, defines the
language that the browser and web server speak to each other. Think of a web
server exactly like a server at a restaurant: when you make a request of him,
he brings it to you. In the context of the internet, the server is bringing
you a web page written in HTML. More on HTML later.

HTTP is a protocol for browsers and servers to talk to each other. Humans,
too, have protocols for talking to each other. Consider that when you meet
someone, you often greet him or her with a handshake. Browsers and servers
also greet and acknowledge each other according to HTTP.

Servers do a lot more than just serve web pages. To accommodate different
types of requests, servers use different ports. The default port number for
HTTP requests is `80`. Navigating to facebook.com is identical to navigating to
`facebook.com:80` because the `80` is implied.

To see HTTP in action, we can fire up a command-line program named telnet. We
open up a terminal window and type `telnet www.facebook.com 80`. This presents
us with a prompt like so:

	Trying 31.13.69.32...
	Connected to star.c10r.facebook.com.
	Escape character is '^]'.
	31.13.69.32 is an IP address. IP stands for internet protocol. An IP address is a unique (more or less) identifier for a computer on the internet. An IP address is to a computer what a mailing address is to a house. In this case, the IP address corresponds to one of Facebook’s servers.

	Now we type the following:

	GET / HTTP/1.1
	Host: www.facebook.com
	In turn, we’ll get a response from the server like this:

	HTTP/1.1 302 Found
	Location: http://www.facebook.com/unsupportedbrowser
	Content-Type: text/html; charset-utf-8
	X-FB-Debug: OigNZFku4U2xO68YDYkoMQs95BMNbmwwMqYVgo0yGx8=
	Date: Wed, 30 Oct 2013 17:20:59 GMT
	Connection: keep-alive
	Content-Length: 0

Facebook doesn’t like the fact that we’re pretending to be a browser, so it’s
redirecting us to a site to tell us that. We can actually trick Facebook into
thinking that we’re coming from a normal browser like Chrome by adding a line
to our HTTP request:

	GET / HTTP/1.1
	Host: www.facebook.com
	User-Agent: Mozilla/5.0 (Macintosh; Indel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36

Note that these user agent strings tell websites a lot about your computer.
In this case, it tells Facebook that we’re using an Intel-based Mac running
OS X 10.8.5 and version 30.0.1599.101 of Chrome.

With this user agent string added to our HTTP request, we get a normal
response back from the server. The server actually still redirects us, this
time to the more secure HTTPS version of the site.

Why do we write GET /? We’re requesting the root of the website. The root of
the site is denoted with a slash just as the root of a hard drive is.

If we switch gears and make an HTTP request to www.mit.edu, we get back an
HTTP response that starts with HTTP/1.1 200 OK and actually contains the HTML
that makes up their homepage. 200 is the "all is well" HTTP status code. You
can see this same HTML if you go to View Source within your browser.

### DNS

How does your browser know the IP address of MIT’s web server? There are
special servers called DNS, or domain name system, servers whose job it is
translate hostnames like `www.mit.edu` into IP addresses.

### TCP/IP

TCP/IP is the protocol that defines how information travels through the
internet. Information travels from source to destination via several routers
in between. Routers are other servers that simply take in bytes and direct
them elsewhere. We can see which routers our information passes through using
a command-line program named traceroute. Each of the lines in the output
represents a router that our request went through. Lines that are just three
asterisks represent routers that ignore this type of request, so we don’t
know where they are. On the right side, there are three time values which
represent three measurements of the number of milliseconds it took to reach
this router.

Typically, information requires fewer than 30 hops between routers to get to
its destination. If we run `traceroute www.mit.edu`, we see that the first few
hops are Harvard’s routers, but by step 6, we’re in New York City. After
that, the hops are obscured.

If we run `traceroute www.stanford.edu`, we see that we can get from Boston
to Washington DC in ~7 steps and less than 15 milliseconds! After that, we
jump to Houston and LAX and finally to Stanford, all in under 90 milliseconds
or so.

There are other machines besides routers that sit between your computer and
the information you’re requesting. For example, that information may live
behind a machine that restricts access known as a firewall. You can think of
an HTTP request as an envelope with the return address being your IP and the
to address being the IP of the web server. A very simple firewall might
reject requests solely based on the IPs they came from, i.e. the return
addresses written on the envelopes. A more advanced firewall might reject
e-mails but not web requests, discriminating using the port number of the
request.

For the sake of efficiency and reliability, HTTP requests are broken up into
chunks of information called packets. These packets don’t have to follow the
same path to reach their destination and some of them never will because they
are dropped by routers in between, whether intentionally or unintentionally.

For a more in-depth look at TCP/IP and the internet, check out [Warriors of
the Net](http://www.youtube.com/watch?v=PBWhzz_Gn10).
