"""Test connection to google & parsing google search result webpage."""
import unittest
try:
    from urllib.urlparse import urlparse
except ImportError:
    from urlparse import urlparse

from pygoogling.googling import GoogleSearch


class GoogleSearchTestCase(unittest.TestCase):
    """Test module by requesting to google page and parse the result."""
    def test_online_search(self):
        """this test is intended to not run on every project test.
        If you want to run the test, you should specifically run this method.
        """
        google_search = GoogleSearch('essanpupil')
        google_search.start_search()
        for item in google_search.search_result:
            url = urlparse(item)
            if url.scheme is not None:
                self.assertIn('http', url.scheme)
            else:
                self.fail('Parsing failed!')
