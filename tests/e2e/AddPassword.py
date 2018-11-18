import unittest
import os
import os.path
import src.config as config
from src.commands.AddCommand import AddCommand
from src.commands.ShowCommand import ShowCommand


class TestAddLoginInfo(unittest.TestCase):
    def test_addLogin(self):
        site = "http://test_site.com/this_login"
        username = "test_user"
        password = "test_password123"

        argument_list = [site, username, password]

        add_command = AddCommand(argument_list)
        add_command.execute()

        show_command = ShowCommand(None)
        stored_logins = show_command.execute()

        self.assertTrue(len(stored_logins) == 1)
        self.assertTrue(stored_logins[0].site == site)
        self.assertTrue(stored_logins[0].username == username)
        self.assertTrue(stored_logins[0].password == password)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(config.VIKING_FILE_PATH):
            os.remove(config.VIKING_FILE_PATH)


if __name__ == '__main__':
    unittest.main()
