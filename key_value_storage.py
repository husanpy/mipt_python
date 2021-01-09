import argparse
import os
import tempfile
import json


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="enter a key alone in order to get value/s for the key")
parser.add_argument("--val", help="enter a value along with key for adding the value to the key")
args = parser.parse_args()
key, val = args.key, args.val


def read_data(storage_path):
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return json.loads(raw_data)
            else:
                return {}
    else:
        return {}


if key and val:
    data = read_data(storage_path)

    if key not in data:
        data[key] = [val]
    else:
        data[key].append(val)

    with open(storage_path, 'w') as f:
        json.dump(data, f)
elif key:
    data = read_data(storage_path)

    if key in data:
        print(*data[key], sep=', ')
    else:
        print(None)
elif val:
    print('you can\'t enter value without key')
