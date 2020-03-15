import threading
import unittest
import urllib.request
from httpservice.app import Server, parsePort
from http.server import HTTPServer
import time

# Extended Class to remove output to stdout in test
class QuietServer(Server):
    def log_message(self, *args):
        pass


class TestRequests(unittest.TestCase):
    def test_shortArgParse(self):
        parser = parsePort(['-p', '9092'])
        self.assertEqual(parser, 9092)


    def setUp(self):
        self.server = HTTPServer(("localhost", 9092), QuietServer)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()


    def test_route_helloworld(self):
        res = urllib.request.urlopen('http://localhost:9092/helloworld')
        self.assertEqual(res.code, 200)
        self.assertEqual(res.read(), bytes('Hello Stranger', 'UTF-8'))


    def test_route_versionz(self):
        route = urllib.request.urlopen('http://localhost:9092/versionz')
        self.assertEqual(route.code, 200)
        

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

        
if __name__ == '__main__':
    unittest.main()