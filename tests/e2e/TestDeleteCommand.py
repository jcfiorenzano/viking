import unittest
import src.secret_manager.SecretManager as SecretManager
from tests.e2e.VikingE2ETestBase import VikingE2ETestBase
from src.model.Secret import Secret


class TestDeleteCommand(VikingE2ETestBase):
    def test_delete_login(self):
        site = "http://test_login.com"
        username = "test_username"
        password = "test_password"

        SecretManager.add(Secret(site, username, password))

        SecretManager.delete(site)

        secrets = SecretManager.get(None)

        self.assertTrue(len(secrets) == 0)


if __name__ == '__main__':
    unittest.main()
