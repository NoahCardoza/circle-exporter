# Circle Exporter

A tiny project to export devices from Circle.

I recently got a new router that could do everything Circle could
do so I needed to remove Circle. However, I had registered over 130 MAC
addressed with Circle and I was not about to copy them over by hand.

# Setup

1. First you'll need to install [Charles](https://www.charlesproxy.com/)
   set up a proxy server and route your phone through it.
   *Google it. There are a lot of tutorials.*

2. Filter out requests starting with `https://10.0.1.20:4567/api/QUERY/all`.

3. Replace `<CIRCLE_URL>` with the URL and voilà!

# Future

I might add a little more to this project if  I have time. Namely,
removing Charles from the equation. However, I'm not sure if this
is going to get much use and I shouldn't ever have to use it
again myself.


