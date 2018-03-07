# coding:utf-8
'''
title:   对KBS项目进行自动发布
author:  Robert
email:luoshuibo@vcredit.compile

'''

import sys
import os
from config import projectmapjson,helpmessage
from time import sleep
import  json

global PROJECT_NAME  ##初始化常量工程名称
global PROJECT_ID  ##初始化常量工程名称编号
global PROJECT_HOME_DIR  ##初始化常量工程根目录
global helpmessage  ##初始化常量帮助提示


projectmapjson = projectmapjson


def action_del(filename):
    '''
        执行删除命令
    '''
    _temp_command = "del/f/s/q " + filename

    output = os.popen(_temp_command)
    print("执行删除命令 ",_temp_command,"    output", output)


    # with os.popen(_command).readlines() as temp_process:
    #     temp_exe_result = temp_process.readlines()
    # print(temp_exe_result)


def set_dir(workdir):
    '''
        执行匹配工程根目录
    '''
    projectdir = str(workdir)
    return projectdir


def set_filename(projectid, mapbody):
    '''
    设置要删除的文件名称
    :param projectid:
    :return: deletefilename
    '''
    deletefilename = mapbody[str(projectid)]["configfile"]
    return deletefilename


def get_dir():
    '''
        执行匹配工程根目录
    '''

    _basedir = os.path.abspath(os.path.dirname(__file__))
    projectdir = os.path.abspath(os.path.dirname(__file__))
    print("获取当前工程根目录  ", projectdir)
    return projectdir


def get_dir_front(tempdir):
    '''
        执行匹配工程根目录的上一级目录
    '''
    _command1 = "cd /d " + tempdir
    print("执行命令",_command1)
    os.popen(_command1)
    sleep(1)
    _command2 = "cd /d  .."
    os.popen("cd /d ..")
    print("执行命令  ",_command2)
    _front_dir = os.getcwd()
    print("上一级目录地址  ", _front_dir)
    return _front_dir


def in_dir(projectdir):
    '''
        进入工程根目录
    '''
    _command = "cd /d " + projectdir
    with os.popen(_command).readlines() as temp_process:
        temp_exe_result = temp_process.readlines()


def action_copy_file(sourcepath, targetpath,excludefile):
    '''
    复制并替换文件
        copy / y d:\test\test.txt d:
    :return:
    '''

    # xcopy yourDir\dir1 otherDir\dir1 /e /s /f /i /y /EXCLUDE:Exclude.txt
    # _temp_command = "xcopy  " + sourcepath + "  " + targetpath+" /e /s /f /i /y \EXCLUDE:"+excludefile
    ## xcopy..D:\Webdeploy\KBSWeb / Y / E / S
    _temp_command = "xcopy  " + sourcepath + "  " + targetpath + " /Y/E/S /EXCLUDE:"+excludefile
    print("复制并替换文件命令  ", _temp_command)
    output = os.popen(_temp_command)
    print("output", output)


# print (output)

if __name__ == '__main__':

    try:
        if sys.argv[1] is not None:
            PROJECT_ID = str(sys.argv[1])
            print("PROJECT_ID", PROJECT_ID)
            print(projectmapjson[PROJECT_ID]["configfile"])
            print(projectmapjson[PROJECT_ID]["targetpath"])
        else:
            PROJECT_ID = int(2)
            print("没有输入工程编号,自动使用默认值2")

    except Exception as e:
        # print(helpmessage["noid"])
        print(e)
        print(json.dumps(helpmessage, sort_keys=True, indent=4, separators=(',', ': '),encoding="gbk",ensure_ascii=True))
        #
        # exit()
    finally:
        print("☆☆☆☆☆☆☆KBS 自动发布☆☆☆☆☆☆☆☆")

    tempdir = get_dir()  ##获取项目工作目录

    print("当前目录 ", tempdir)

    newdir = get_dir_front(tempdir)
    print("上一层目录 ", newdir)

    tempfilename = set_filename(PROJECT_ID, projectmapjson)  ##获取要删除的文件名称

    action_del(tempfilename)  ##执行删除


    tempexcludefile = tempdir+"\\"+projectmapjson[PROJECT_ID]["excludefile"]
    action_copy_file(newdir, projectmapjson[PROJECT_ID]["targetpath"],tempexcludefile)  ##复制并替换编译后的文件


