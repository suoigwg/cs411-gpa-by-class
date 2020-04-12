import os
import json


DATA_FOLDER = "data/"


def write_to_file(content, path, replace=False):
    if not replace and os.path.exists(path):
        print(f'{path} already exists')
        return
    else:
        print(f'Writing: {path}')
        with open(path, 'w') as f:
            f.write(json.dumps(content))


def read_json_from_file(path):
    if os.path.exists(path):
        print(f'Reading: {path}')
        with open(path, 'r') as f:
            content = f.read()
            return json.loads(content)
    else:
        print(f'File: {path} does not exist')
