import unittest
from urlparse import urlparse

from pygoogling.googling import GoogleSearch


class GoogleSearchTestCase(unittest.TestCase):
    def online_testcase(self):
        # this test is intended to not run on every project test.
        # If you want to run the test, you should specifically run this method
        gs = GoogleSearch('essanpupil')
        gs.start_search()
        for item in gs.search_result:
            url = urlparse(item)
            if url.scheme is not None:
                self.assertIn('http', url.scheme)
            else:
                self.fail('Parsing failed!')
