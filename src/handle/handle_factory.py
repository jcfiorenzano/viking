from src.handle.add_secret_handle import AddCommandHandle
from src.handle.get_secret_handle import ShowCommandHandle
from src.handle.delete_secret_handle import DeleteCommandHandle


def create_handle(parsed_object):
    if parsed_object.add:
        return AddCommandHandle(parsed_object.add)
    elif parsed_object.show:
        return ShowCommandHandle(parsed_object.show)
    elif parsed_object.delete:
        return DeleteCommandHandle(parsed_object.delete)
