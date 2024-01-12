import magic

def guess_file_type(file_path):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
        return magic.from_buffer(file_bytes, mime=True)
    

if __name__ == '__main__':
    file_type = guess_file_type('file_storage/test.txt')
    print(file_type)