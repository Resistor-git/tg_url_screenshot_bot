import unittest

from helpers import address_formatter


class TestAddressFormatter(unittest.TestCase):
    def test_address_formatter_http(self):
        url = "http://something.com"
        self.assertEqual(address_formatter(url), "http://something.com")

    def test_address_formatter_https(self):
        url = "https://something.com"
        self.assertEqual(address_formatter(url), "https://something.com")

    def test_address_formatter_www(self):
        url = "www.something.com"
        self.assertEqual(address_formatter(url), "https://www.something.com")

    def test_address_formatter_no_protocol(self):
        url = "something.com"
        self.assertEqual(address_formatter(url), "https://something.com")
