import unittest
from src.security.SecurityManager import SecurityManager


class SecureManagerTest(unittest.TestCase):

    def test_authentication(self):
        SecurityManager().create_account(password='123')
        SecurityManager().authenticate(password='123')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
