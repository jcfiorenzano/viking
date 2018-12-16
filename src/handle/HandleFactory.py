from src.handle.AddCommandHandle import AddCommandHandle
from src.handle.ShowCommandHandle import ShowCommandHandle
from src.handle.DeleteCommandHandle import DeleteCommandHandle


class HandleFactory:
    @staticmethod
    def create_handle(parsed_object):
        if parsed_object.add:
            return AddCommandHandle(parsed_object.add)
        elif parsed_object.show:
            return ShowCommandHandle(parsed_object.show)
        elif parsed_object.delete:

            return DeleteCommandHandle(parsed_object.delete)
