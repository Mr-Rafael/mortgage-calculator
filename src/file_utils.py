import os

def create_directory_if_nonexistent(path):
    print(f"received path {path}")
    split_path = path.split("/")
    print(f"Attempting to create the directory with split path {path.split("/")}")
    current_path = ""
    for section in split_path:
        print(f"checking path {current_path}{section}")
        current_path = f"{current_path}{section}"
        if not os.path.isdir(current_path):
            print(f"the path {current_path} doesn't exist. creating it.")
            os.mkdir(current_path, mode=0o777)
        current_path = f"{current_path}/"

def write_file(full_file_path, content):
    with(open(full_file_path, 'w') as html_file):
        html_file.write(content)