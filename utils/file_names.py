from hashlib import sha256
from time import time

def get_storage_filename(filename, ext):
    file_name = sha256(f'{filename}{time()}'.encode()).hexdigest()
    return file_name + ext
    

if __name__ == '__main__':
    name = get_storage_filename('test', ".txt")
    print(name)