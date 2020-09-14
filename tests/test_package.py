# pylint: disable=R0201,E1101

import os
import unittest

from whois import Whois


class TestWhois(unittest.TestCase):
    def test_api_token(self):
        if os.environ.get('PROMPTAPI_TOKEN', None):
            os.environ['PROMPTAPI_TOKEN'] = ''  # noqa: S105

        who = Whois()
        response = who.check('promptapi.com')

        self.assertTrue(response.get('error', None))


if __name__ == '__main__':
    unittest.main()
