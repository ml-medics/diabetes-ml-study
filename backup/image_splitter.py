from shutil import rmtree, copyfile
from os import listdir, mkdir, remove, unlink
from os.path import join, isfile, isdir, exists, dirname, realpath
import pandas as pd


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


def copy_file(src_dir, dst_dir):
    copyfile(src_dir, dst_dir)


df = pd.read_csv('trainLabels.csv')
print(df)

base_dir_path = dirname(realpath(__file__))
image_dir_path = join(base_dir_path, 'eye data', 'train')


for index, row in df.iterrows():

    image_name = row['image']
    level = row['level']
    dir_path = join(base_dir_path, str(level))
    src_image_path = join(image_dir_path, image_name + '.jpeg')
    dst_image_path = join(dir_path, image_name + '.jpeg')

    print(src_image_path)

    if not exists(dir_path):
        make_dir_helper(dir_path)

    if exists(src_image_path):
        copy_file(src_image_path, dst_image_path)

