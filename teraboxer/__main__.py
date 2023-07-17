import argparse
import os

from . import TeraBox

parser = argparse.ArgumentParser("TeraBoxer", )

parser.add_argument("file_path", help="path of the file that need to be uploaded")
parser.add_argument('--ndus',default=None, help="ndus key from terabox cookies")

args = parser.parse_args()
print(args.ndus or os.environ['TERABOX_KEY'])
tb = TeraBox(args.ndus or os.environ['TERABOX_KEY'])
tb.upload_file(args.file_path)