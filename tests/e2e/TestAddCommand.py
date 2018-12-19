import unittest
import src.secret_manager.SecretManager as SecretManager
from src.model.Secret import Secret
from tests.e2e.VikingE2ETestBase import VikingE2ETestBase


class TestAddCommand(VikingE2ETestBase):
    def test_addLogin(self):
        site = "http://test_site.com/this_login"
        username = "test_user"
        password = "test_password123"

        secret = Secret(site, username, password)
        SecretManager.add(secret)

        stored_secrets = SecretManager.get(None)

        self.assertTrue(len(stored_secrets) == 1)
        self.assertTrue(stored_secrets[0].site == site)
        self.assertTrue(stored_secrets[0].username == username)
        self.assertTrue(stored_secrets[0].password == password)

    def test_addlogin_incremental(self):
        SecretManager.add(Secret("http://test_login.com", "username", "password"))
        SecretManager.add(Secret("http://test_login2.com", "username", "password"))
        SecretManager.add(Secret("http://test_login3.com", "username", "password"))

        stored_secrets = SecretManager.get(None)

        self.assertTrue(len(stored_secrets) == 3)


if __name__ == '__main__':
    unittest.main()
