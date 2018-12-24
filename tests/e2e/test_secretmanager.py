import unittest
import viking.secret_manager.secret_manager as SecretManager
from viking.model.secret import Secret
from tests.e2e.testbase import TestBase


class TestSecretManager(TestBase):
    def test_add(self):
        site = "http://test_site.com/this_login"
        username = "test_user"
        password = "test_password123"

        secret = Secret(site, username, password)
        SecretManager.add(secret)

        stored_secrets = SecretManager.get_all()

        self.assertTrue(len(stored_secrets) == 1)
        self.assertTrue(stored_secrets[0].site == site)
        self.assertTrue(stored_secrets[0].username == username)
        self.assertTrue(stored_secrets[0].password == password)

    def test_add_multiple(self):
        SecretManager.add(Secret("http://test_login.com", "username", "password"))
        SecretManager.add(Secret("http://test_login2.com", "username", "password"))
        SecretManager.add(Secret("http://test_login3.com", "username", "password"))

        stored_secrets = SecretManager.get_all()

        self.assertTrue(len(stored_secrets) == 3)

    def test_delete(self):
        site = "http://test_login.com"
        username = "test_username"
        password = "test_password"

        SecretManager.add(Secret(site, username, password))

        SecretManager.delete(site)

        secrets = SecretManager.get_all()

        self.assertTrue(len(secrets) == 0)
        
        
if __name__ == '__main__':
    unittest.main()
