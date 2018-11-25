import unittest
import os
import src.config as config


class VikingE2ETestBase(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        if os.path.exists(config.VIKING_FILE_PATH):
            os.remove(config.VIKING_FILE_PATH)
        if os.path.exists(config.ACCOUNT_FILE_PATH):
            os.remove(config.ACCOUNT_FILE_PATH)