"""

A simple HTTP request logger to log messages sent by the instrumentation.

Author: Brian Tuan

Last Modified: May 29, 2017

"""

import click
import json
import time

from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus as HTTP


def process_POST(data):
    if 'HIT_ID' not in data or 'action' not in data:
        return

    t_received = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    with open("{}.log".format(data['HIT_ID']), 'a') as f:
        f.write("{}\n{}\n\n".format(t_received, data['action']))


class InstrumentationHandler(SimpleHTTPRequestHandler):
    def respond(self):
        self.send_response(HTTP.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        self.respond()
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8'))
        process_POST(data)


@click.command()
@click.option("-v", "--verbose", default=True, is_flag=True, help="Toggle for verbosity.")
def run(verbose):
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, InstrumentationHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
