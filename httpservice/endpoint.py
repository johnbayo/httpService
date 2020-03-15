from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import re
import json
import logging
import argparse, os, sys


HOST_NAME = 'localhost'


def parsePort(someArgs=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--PORT',dest='PORT', type=int, default=os.environ.get('HTTP_SERVICE_PORT', 8080))
    args = parser.parse_args(someArgs)
    return args.PORT


class Server(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    		

    def do_GET(self):
        self.parsed_path = urlparse(self.path)
        self.query = parse_qs(self.parsed_path.query)
        try:
            if self.parsed_path.path == "/helloworld":
                if not bool(self.query):
                    self._set_response()
                    message = bytes("Hello Stranger", 'UTF-8')
                    self.wfile.write(message)
                    return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)