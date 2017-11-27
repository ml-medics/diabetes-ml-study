from shutil import rmtree
from os import listdir, mkdir, remove, unlink
from os.path import join, isfile, isdir, exists


def make_dir_helper(dir_path):
    if not exists(dir_path):
        mkdir(dir_path)
        return True
    return False


def delete_dir_helper(dir_path):
    if exists(dir_path):
        rmtree(dir_path)
        return True
    return False


def delete_dir_files_helper(dir_path):
    for file in listdir(dir_path):
        file_path = join(dir_path, file)
        try:
            if isfile(file_path):
                unlink(file_path)
        except Exception as e:
            print(e)



def is_jpeg(fname):
    return fname.split('.')[-1] == 'jpg'
