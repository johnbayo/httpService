from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import re
import json
import logging
import argparse, os, sys


HOST_NAME = 'localhost'

#argparse library to check port, converted to function for testing purpose
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
    

    def camel_case_split(self, str):   
        return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str) 


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
                elif 'name' in self.query:
                    self._set_response()
                    partStr = self.query['name'][0]
                    msg = self.camel_case_split(partStr)
                    newMsg=' '.join(msg)
                    message = bytes(newMsg, 'UTF-8')
                    self.wfile.write(message)
                    return
                else:
                    raise IOError
            elif self.parsed_path.path == "/versionz":
                self._set_response()
                message = {
                    'name': httpservice.__name__,
                    'version': httpservice.__version__
                }
                self.wfile.write(json.dumps(message).encode("utf-8"))
                return
            else:
                raise IOError
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

            
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s" % (self.address_string(),self.log_date_time_string(),format%args))


def getVersion():
    from subprocess import check_output
    try:
        version = check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()
    except:
        version = '0.01'
    return version		


def main():
    PORT_NUMBER = parsePort(sys.argv[1:])
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("myhttpService.log"),
            logging.StreamHandler()
        ]
    )
    
    print('Server UP at %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        print("server up")
        httpd.serve_forever()
        print("server up")
    except KeyboardInterrupt:
        httpd.server_close()
        logging.info("Done!")
        print('Control ^C Detected. Server DOWN')