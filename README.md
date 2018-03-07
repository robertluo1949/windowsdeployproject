title:KBS 测试脚本
      包括编译发布的脚本
author:罗水波



使用说明:  python KBSAutoDeploy.py  1
末尾的数值1 是项目编号目前支持 [1,2,3,4,5] 。后期会按需要依次增加。


项目结构: (最简单的测试脚本工程，不采用大型项目的mvc模式，也不采用其他多层文件目录方式)
1  配置文件 config.py
2  部署后的操作 (删除测试脚本和多余文件)KBSAfterAutoDeploy.py
3  自动部署操作 KBSAutoDeployKKG.py
4  自动部署造单工具
5  说明文档  README.md
6  xcopy 的排除文件清单   uncopy.txt

