import unittest
from logging import getLogger as get_logger
logger = get_logger(__name__)


class TestCaseWithDebugLogging(unittest.TestCase):
    def assertEqual(self, got, expected, msg=None):
        logger.debug("got %s", got)
        logger.debug("expected %s", expected)
        return super().assertEqual(got, expected, msg=msg)

    def assertDictEqual(self, got, expected, msg=None):
        logger.debug("got %s", got)
        logger.debug("expected %s", expected)
        return super().assertDictEqual(got, expected, msg=msg)
