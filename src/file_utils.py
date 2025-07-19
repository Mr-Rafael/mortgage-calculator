import os
import json
from dataclasses import asdict
from decimal import Decimal

def create_directory_if_nonexistent(path):
    print(f"received path {path}")
    split_path = path.split("/")
    current_path = ""
    for section in split_path:
        current_path = f"{current_path}{section}"
        if not os.path.isdir(current_path):
            os.mkdir(current_path, mode=0o777)
        current_path = f"{current_path}/"

def write_file(full_file_path, content):
    with(open(full_file_path, 'w') as html_file):
        html_file.write(content)

def dump_json(full_file_path, object):
    with open(full_file_path, "w") as f:
        json.dump(asdict(object), f, indent=4, cls=DecimalEncoder)

def get_all_files_in_directory(directory):
    files_list = os.listdir(directory)
    mortgage_files = []
    for file in files_list:
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and full_path.endswith(".mortgage.json"):
            mortgage_files.append(file.split(".")[0])
    return mortgage_files

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)  # or float(obj) for numbers
        return super().default(obj)