from io import BytesIO
from uuid import UUID, uuid4
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
temp_files_dir = os.path.join(current_dir, 'temp_files')
os.makedirs(temp_files_dir, exist_ok=True)

print(f'{temp_files_dir=}')

def get_temp_file_name(file_id: str, file_ext=""):   
    print(os.listdir(temp_files_dir))
    file_path = os.path.join(temp_files_dir, f'{file_id}{file_ext}')

    return file_path


def create_temp_bin_file(file_io: BytesIO) -> str:
    file_id = str(uuid4())
    file_path = f"./temp_files/{file_id}"

    with open(file_path, 'ab') as file:
        file.write(file_io.read())
    
    os.chmod(file_path, 0o644)
    
    return file_id

def read_temp_bin_file(file_id: str) -> bytes | None:
    file_content = None
    file_path = f"./temp_files/{file_id}"
    with open(file_path, 'rb') as file:
        file_content = file.read()
        os.remove(file_path)
    
    return file_content
