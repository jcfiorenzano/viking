import unittest
from tests.e2e.VikingE2ETestBase import VikingE2ETestBase
from src.commands.AddCommand import AddCommand
from src.commands.DeleteCommand import DeleteCommand
from src.commands.ShowCommand import ShowCommand


class TestDeleteLogin(VikingE2ETestBase):
    def test_delete_login(self):
        site = "http://test_login.com"
        username = "test_username"
        password = "test_password"

        addComand = AddCommand([site, username, password])
        addComand.execute()

        delete_command = DeleteCommand([site])
        delete_command.execute()

        show_command = ShowCommand(None)
        logins = show_command.execute()

        self.assertTrue(len(logins) == 0)


if __name__ == '__main__':
    unittest.main()