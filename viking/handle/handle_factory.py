from viking.handle.add_secret_handle import AddCommandHandle
from viking.handle.get_secret_handle import ShowCommandHandle
from viking.handle.delete_secret_handle import DeleteCommandHandle
from viking.handle.add_secret_handle import AddCommandHandle

def create_handle(parsed_object):
    if parsed_object.add is not None:
        return AddCommandHandle(parsed_object.add)
    elif parsed_object.show is not None:
        return ShowCommandHandle(parsed_object.show)
    elif parsed_object.delete is not None:
        return DeleteCommandHandle(parsed_object.delete)
