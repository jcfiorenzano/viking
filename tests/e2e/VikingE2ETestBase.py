import unittest
import os
import src.config as config
import src.security.SecurityManager as SecurityManager


class VikingE2ETestBase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        if os.path.exists(config.VIKING_FILE_PATH):
            os.remove(config.VIKING_FILE_PATH)

        if os.path.exists(config.ACCOUNT_FILE_PATH):
            os.remove(config.ACCOUNT_FILE_PATH)

        SecurityManager.create_account("test_password123")
        SecurityManager.authenticate("test_password123")

    @classmethod
    def tearDown(cls):
        if os.path.exists(config.VIKING_FILE_PATH):
            os.remove(config.VIKING_FILE_PATH)
        if os.path.exists(config.ACCOUNT_FILE_PATH):
            os.remove(config.ACCOUNT_FILE_PATH)
