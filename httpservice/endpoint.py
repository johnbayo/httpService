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
    		
