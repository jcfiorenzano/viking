import unittest
from src.commands.AddCommand import AddCommand
from src.commands.ShowCommand import ShowCommand
from tests.e2e.VikingE2ETestBase import VikingE2ETestBase


class TestAddCommand(VikingE2ETestBase):
    def test_addLogin(self):
        site = "http://test_site.com/this_login"
        username = "test_user"
        password = "test_password123"

        add_command = AddCommand(site, username, password)
        add_command.execute()

        show_command = ShowCommand(None)
        stored_logins = show_command.execute()

        self.assertTrue(len(stored_logins) == 1)
        self.assertTrue(stored_logins[0].site == site)
        self.assertTrue(stored_logins[0].username == username)
        self.assertTrue(stored_logins[0].password == password)

    def test_addlogin_incremental(self):

        add_command = AddCommand("http://test_login.com", "username", "password")
        add_command.execute()

        add_command = AddCommand("http://test_login2.com", "username", "password")
        add_command.execute()

        add_command = AddCommand("http://test_login3.com", "username", "password")
        add_command.execute()

        show_command = ShowCommand(None)
        stored_logins = show_command.execute()

        self.assertTrue(len(stored_logins) == 3)


if __name__ == '__main__':
    unittest.main()
