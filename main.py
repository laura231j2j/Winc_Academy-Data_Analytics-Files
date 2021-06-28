__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Creating empty folder 'cache' in current directory
import os
from os import listdir
import shutil
from zipfile import ZipFile

location = os.getcwd()
dir_path = os.path.join(location, 'cache')
zip_file = './files/data.zip'


def clean_cache():
    if 'cache' in os.listdir():
        shutil.rmtree(dir_path, ignore_errors=False)
    return os.mkdir('cache')


clean_cache()

# Function that unpacks a zip file into a clean cache folder.


def cache_zip(zip_file, dir_path):
    with ZipFile(zip_file, 'r',) as zip:
        return zip.extractall(dir_path)


# Return a list of all the files in the cache
def cached_files():
    list_absolute_paths = []
    for file in listdir(dir_path):
        absolute_path_file = os.path.join(dir_path, file)
        list_absolute_paths.append(absolute_path_file)
    return list_absolute_paths


# Find the password
def find_password(cached_files=cached_files()):
    for file in cached_files:
        with open(file) as f:
            if 'password' in f.read():
                with open(str(file)) as lines:
                    for line in lines:
                        if 'password' in line:
                            password = line.strip('password: ').strip()
                            return password


# Main

cache_zip(zip_file, dir_path)
print(cached_files())
print(find_password(cached_files()))
