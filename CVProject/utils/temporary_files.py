from io import BytesIO
from uuid import UUID, uuid4
import os

def resolve_temp_files_folder():
    os.makedirs("temp_files", exist_ok=True)


def create_temp_bin_file(file_io: BytesIO) -> str:
    file_id = str(uuid4())
    resolve_temp_files_folder()
    with open(f"temp_files/{file_id}", 'ab') as file:
        file.write(file_io.read())
    
    return file_id

def read_temp_bin_file(file_id: str) -> bytes | None:
    file_content = None
    file_path = f"temp_files/{file_id}"
    resolve_temp_files_folder()
    with open(file_path, 'rb') as file:
        file_content = file.read()
        os.remove(file_path)
    
    return file_content
