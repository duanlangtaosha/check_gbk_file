#! -*-coding:utf-8 -*-

import sys
import os
import re

def __get_source_files_recursive(dir_path_list, ignor_dir_path_list):
    list_source_files = []
    patt = '(.+\.c)$|(.+\.C)$|(.+\.S)$|(.+\.s)$|(.+\.cpp)$|(.+\.CPP)$|(.+\.h)$|(.+\.H)$'
    isbreak = False
    for dir_path in dir_path_list:
        for fpath, dir, fs in os.walk(dir_path):
            for ignor_dir_path in ignor_dir_path_list:

                #发现是忽略目录就退出，当前循环
                if ignor_dir_path in fpath :
                    isbreak = True
                    break;

            #如果里层循环跳出，则此层循环continue
            if  isbreak == True:
                isbreak = False
                continue;
            print fpath
            for f in fs:
                m = re.match(patt, f)
                if m != None:
                    list_source_files.append(os.path.join(fpath, f))

    return list_source_files


def __check_file(file_path):
    isok = True
    with open(file_path, u"rb") as fd:
        content = fd.read()
        try:
            content.decode(u"GBK")
        except UnicodeDecodeError as e:
            # print e
            print ("the %s format is incorrect! Please modify the file farmat is the GBK!"%file_path)
            isok = False
    return isok

def __check_files(list_file):
    isok = True
    for f in list_file:
        if __check_file(f) == False:
            isok = False
    if isok == False:
        sys.exit(-1)


# files = glob.glob(r"G:\Desktop\wchar\*.c")
# print __get_source_files_recursive([r"G:\Desktop\wchar"],[r"G:\Desktop\wchar\wchar_test_gcc"])
# print os.walk(r"G:\Desktop\wchar")

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

    __check_files(__get_source_files_recursive([ur"G:\Desktop\wchar"], [r"G:\Desktop\wchar\wchar_test_gcc"]))

    # print __get_source_files_recursive([ur"G:\Desktop\wchar"], [r"G:\Desktop\wchar\wchar_test_gcc"])