# coding:utf-8
'''
title:   对KBS项目进行自动发布之后,删除多余的文件
author:  Robert
email:luoshuibo@vcredit.compile

'''

from config import projectmapjson,helpmessage
import sys,os


global PROJECT_NAME  ##初始化常量工程名称
global PROJECT_ID  ##初始化常量工程名称编号
global PROJECT_HOME_DIR  ##初始化常量工程根目录
global helpmessage  ##初始化常量帮助提示



def get_testfilenum(projectid,countnum):
    '''
    执行获取文件命令
    :param projectid:
    :return:
    '''
    delfilename =projectmapjson[PROJECT_ID]["deploypath"]+"\\"+projectmapjson[PROJECT_ID]["testfiledir"][countnum]
    print("获得要删除的文件地址",delfilename)
    return delfilename

def action_del_file(filename):
    '''
    执行删除文件命令
    :param filename:
    :return:
    '''

    _temp_command = "del /q/a/f " + filename +"\\*.*"

    output = os.popen(_temp_command)
    print("删除文件: output", output)


def action_del_dir(filename):
    '''
    执行删除文件夹命令
    :param filename:
    :return:
    '''

    _temp_command = "rd /s/q " + filename

    output = os.popen(_temp_command)
    print("删除文件夹:  output", output)






if __name__ == '__main__':

    try:
        if sys.argv[1] is not None:
            PROJECT_ID = str(sys.argv[1])
            print("PROJECT_ID", PROJECT_ID)
            print(projectmapjson[PROJECT_ID])

        else:
            PROJECT_ID = int(0)
            print("没有输入工程编号,自动使用默认值2")

    except Exception as e:
        PROJECT_ID = int(0)
        print(helpmessage["noid"])
        print(e)
        #
        # exit()
    finally:
        print("☆☆☆☆☆☆☆KBS 自动发布☆☆☆☆☆☆☆之后")




    tempdi =projectmapjson[PROJECT_ID]["testfiledir"]

    len_temfile = len(projectmapjson[PROJECT_ID]["testfiledir"])
    print("长度",len_temfile,"当前测试脚本文件",tempdi)


    count = 0   ##计数器
    while count < len_temfile:
        print("计数器",count, " 小于 ",len_temfile)
        delfile = get_testfilenum(PROJECT_ID, count)
        action_del_file(delfile)
        action_del_dir(delfile)

        count = count + 1
    else:
        print(count, " 大于或等于 ",len_temfile)
    # action_del_file((projectmapjson[PROJECT_ID]["deploypath"]+"\\"+))
