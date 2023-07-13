from pathlib import Path
from . import endpoints
import os.path

def file_obj_upload(ndus, file_obj, file_name, size, destination_dir='/'):
    destionation_path = Path(destination_dir) / file_name
    pc = endpoints.pre_create(ndus, destionation_path)
    upload_id = pc['uploadid']
    sf2 = endpoints.superfile2(ndus, destionation_path, upload_id, file_obj)
    md5 = sf2['md5']
    c = endpoints.create(ndus, destionation_path, md5, upload_id, size)
    return c

def file_upload(ndus, file_path, destination_dir='/', rename=None):
    file_path = Path(file_path)
    size = os.path.getsize(file_path)
    with open(file_path, 'rb') as file:
        return file_obj_upload(ndus, file, rename or file_path.name, size, destination_dir=destination_dir)