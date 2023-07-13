from . import actions

class TeraBox:
    def __init__(self, ndus):
        self.__ndus = ndus

    def upload_file_obj(self, file_obj, file_name, size, destination_dir='/'):
        return actions.file_obj_upload(self.__ndus, file_obj, file_name, size, destination_dir)
    
    def upload_file(self, file_path, destination_dir='/', rename=None):
        return actions.file_upload(self.__ndus, file_path, destination_dir, rename)
    