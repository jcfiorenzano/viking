import unittest
import os
import src.config as config


class VikingE2ETestBase(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(config.VIKING_FILE_PATH):
            os.remove(config.VIKING_FILE_PATH)