# HTMLLogger

A HTML logging server, based on python's built-in HTML server. Once running, the server will respond to HTML GET requests for /index.html, and record all actions with the page via POST callbacks. The page itself is linked to a HIT worker ID, destined for instrumentation with Amazon MTurk.

## Running it
```
$ pip3 install -r requirements.txt
$ python3 logger.py
```

On a browser, navigate to http://localhost:8000/index.html.

That's it!

## Modifying the Forms
All that is required to log actions with a certain element of the page is to add the ".listened" class to the HTML tag. An inline Javascript element will fire POST calls back to the server, imbued with whatever value the "id" attribute of the HTML tag clicked on has.

All actions are associated with the HIT worker ID, and are logged to `<ID>.log`. For example, if a HIT worker enters ID: 123, all actions will be logged to a local file at `123.log`


