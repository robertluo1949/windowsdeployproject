# coding:utf-8
'''
title:   对KBS项目进行自动发布
author:  Robert
email:luoshuibo@vcredit.compile

'''

##项目工程的基础配置


projectmapjson = {
    "0": {
        "progectname": "null",
        "configfile": "null",
        "sourcetpath": "null",
        "targetpath": "null",
        "deploypath": "null",
        "excludefile": "null",
        "testfiledir": ["null", "null"]

    },
    "1": {
        "progectname": "KBSWEB",
        "configfile": "..\\Web.config",
        "sourcetpath": "..\\*.*",
        "targetpath": "D:\\Web\\KBSWeb",
        "deploypath": "D:\\Web\\KBSWeb",
        "excludefile": "uncopy.txt",
        "testfiledir":["testscripts","testscripts@tmp"]

    },
    "2": {
        "progectname": "KBSMSA",
        "configfile": "..\\Web.config",
        "sourcetpath": "..\\*.*",
        "targetpath": "D:\\Web\\KBSMSA",
        "deploypath": "D:\\Web\\KBSMSA",
        "excludefile": "uncopy.txt",
        "testfiledir": ["testscripts", "testscripts@tmp"]
    },
    "3": {
        "progectname": "KBSAutoJob",
        "configfile": "..\\KKD.BusinessSystem.AutoJob.exe.config",
        "sourcetpath": "..\\*.*",
        "deploypath": "D:\\Web\\KKD.BusinessSystem.AutoJob",
        "targetpath": "D:\\Web\\KKD.BusinessSystem.AutoJob",
        "excludefile": "uncopy.txt",
        "testfiledir": ["testscripts", "testscripts@tmp"]
    },
    "4": {
        "progectname": "KBSWEBAPI",
        "configfile": "..\\Web.config",
        "sourcetpath": "..\\*.*",
        "deploypath": "D:\\Web\\KBSWebApi",
        "targetpath": "D:\\Web\\KBSWebApi",
        "excludefile": "uncopy.txt",
        "testfiledir": ["testscripts", "testscripts@tmp"]
    },
    "5": {
        "progectname": "KBSContractParts",
        "configfile": "..\\Web.config",
        "sourcetpath": "..\\*.*",
        "deploypath": "D:\Document\合同",
        "targetpath": "D:\Document\合同",
        "excludefile": "uncopy.txt",
        "testfiledir": ["testscripts", "testscripts@tmp"]
    },
    "6": {
        "progectname": "KBSContractParts",
        "configfile": "..\\Web.config",
        "sourcetpath": "..\\*.*",
        "deploypath": "null",
        "targetpath": "null",
        "excludefile": "uncopy.txt",
        "testfiledir": ["testscripts", "testscripts@tmp"]
    },
    "7": {
        "progectname": "null",
        "configfile": "null",
        "sourcetpath": "null",
        "targetpath": "null",
        "deploypath": "null",
        "excludefile": "null",
        "testfiledir": ["null", "null"]

    },
    "8": {
        "progectname": "null",
        "configfile": "null",
        "sourcetpath": "null",
        "targetpath": "null",
        "deploypath": "null",
        "excludefile": "null",
        "testfiledir": ["null", "null"]

    },
    "9": {
        "progectname": "null",
        "configfile": "null",
        "sourcetpath": "null",
        "targetpath": "null",
        "deploypath": "null",
        "excludefile": "null",
        "testfiledir": ["null", "null"]

    }

}



##帮助文案提示
helpmessage = {
    "noid": {"事项": "没有输入工程编号参数",
             "1": "KBSWEB 网站界面",
             "2": "KBSMSA 系统微服务",
             "3": "KBSAutoJob 自动跑批JOB",
             "4": "KBSWEBAPI  去VBS占位接口",
             "5": "KBSContractParts  合同套件",
             "6": "待定",
             "7": "待定",
             "8": "待定",
             "9": "待定"
             }
}



