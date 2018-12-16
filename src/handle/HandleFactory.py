from src.commands.ShowCommand import ShowCommand
from src.commands.DeleteCommand import DeleteCommand
from src.handle.AddCommandHandle import AddCommandHandle
from src.handle.ShowCommandHandle import ShowCommandHandle
from src.handle.DeleteCommandHandle import DeleteCommandHandle


class HandleFactory:
    @staticmethod
    def create_handle(parsed_object):
        if parsed_object.add:
            return AddCommandHandle(parsed_object.add)
        elif parsed_object.show:
            site_url = parsed_object.show[0] if parsed_object.show is not None else None
            show_command = ShowCommand(site_url)
            return ShowCommandHandle(show_command)
        elif parsed_object.delete:
            site_url = parsed_object.delete[0]
            delete_command = DeleteCommand(site_url)
            return DeleteCommandHandle(delete_command)
