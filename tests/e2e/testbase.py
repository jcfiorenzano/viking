import unittest
import os
import viking.config as config
import viking.security.security_manager as SecurityManager


class TestBase(unittest.TestCase):

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
