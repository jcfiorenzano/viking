from src.commands.AddCommand import AddCommand
from src.commands.ShowCommand import ShowCommand
from src.commands.DeleteCommand import DeleteCommand
from src.handle.AddCommandHandle import AddCommandHandle
from src.handle.ShowCommandHandle import ShowCommandHandle
from src.handle.DeleteCommandHandle import DeleteCommandHandle


class HandleFactory:
    @staticmethod
    def create_handle(parsed_object):
        if parsed_object.add:
            site_url = parsed_object.add[0]
            username = parsed_object.add[1]
            password = parsed_object.add[2] if len(parsed_object.add) == 3 else None
            add_command = AddCommand(site_url, username, password)
            return AddCommandHandle(add_command)
        elif parsed_object.show:
            site_url = parsed_object.show[0] if parsed_object.show is not None else None
            show_command = ShowCommand(site_url)
            return ShowCommandHandle(show_command)
        elif parsed_object.delete:
            site_url = parsed_object.delete[0]
            delete_command = DeleteCommand(site_url)
            return DeleteCommandHandle(delete_command)
