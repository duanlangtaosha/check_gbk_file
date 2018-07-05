#! -*-coding:utf-8 -*-

import os
import sys
import os
import glob
import re

def __get_source_files_recursive(dir_path):
    list_source_files = []
    for fpath, dir, fs in os.walk(dir_path):
        patt = '(.+\.c)$|(.+\.C)$|(.+\.S)$|(.+\.s)$|(.+\.cpp)$|(.+\.CPP)$|(.+\.h)$|(.+\.H)$'
        for f in fs:
            m = re.match(patt, f)
            if m != None:
                list_source_files.append(os.path.join(fpath, f))

    return list_source_files


def __check_file(file_path):
    with open(file_path, u"rb") as fd:
        content = fd.read()
        try:
            content.decode(u"GBK")
        except UnicodeDecodeError as e:
            # print e
            print ("the %s format is incorrect! Please modify the file farmat is the GBK!"%file_path)

def __check_files(list_file):
    for f in list_file:
        __check_file(f)

    pass

# files = glob.glob(r"G:\Desktop\wchar\*.c")
print __get_source_files_recursive(r"G:\Desktop\wchar")
print os.walk(r"G:\Desktop\wchar")

if __name__ == "__main__":

    # with open(u"main.c", u"rb") as fd:
    #     content = fd.read()
    #     print content
    #
    #     try:
    #         content.decode(u"GBK")
    #     except UnicodeDecodeError as e:
    #         print e
    #         print ("the file format is incorrect!")
    #     pass
    #
    # print("Hello World")
    # pass

    __check_files(__get_source_files_recursive(ur"G:\Desktop\wchar"))