from tqdm.utils import CallbackIOWrapper
from tqdm import tqdm
import argparse
import os

from . import TeraBox

parser = argparse.ArgumentParser("TeraBoxer", )

parser.add_argument("file_path", help="path of the file that need to be uploaded")
parser.add_argument('--ndus',default=None, help="ndus key from terabox cookies")

args = parser.parse_args()
tb = TeraBox(args.ndus or os.environ['TERABOX_KEY'])
file = args.file_path
file_size = os.stat(file).st_size
base_name = os.path.basename(file)
with open(file, 'rb') as f:
    with tqdm(total=file_size, unit_scale=True, unit='B', unit_divisor=1024, desc=base_name) as progress:
        wrapped_file = CallbackIOWrapper(progress.update, f, "read")
        tb.upload_file_obj(wrapped_file,base_name,file_size)
