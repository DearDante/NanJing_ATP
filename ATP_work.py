# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:07:34 2018
工作流程：
1.获取原始atp文件
2.获取工作模式
3.获取新atp文件
4.生成pl4文件
5.解析pl4文件，生成结果
6.删除pl4文件，回到步骤3
7.200次仿真结束。
@author: 43926
"""

import create_ATP as cATP
import run_ATP as rATP
import pl4_Analysis as pA
import os

class atp_work(object):
    def __init__(self,ATPfile,ATPmodel):
        self.filename = ATPfile
        self.__ori_atp = cATP.create_ATP(self.filename)                #创建一个atp对象
        self.__ori_atp.get_model(ATPmodel)                       #获取工作模式
    
    def main_work(self,n):
        for i in range(n):
            self.__ori_atp.set_atp()                            #设置新的开关协议
            self.__ori_atp.generate(i)                          #生成新的atp文件
            rATP.run_ATP(self.filename)                         #生成pl4文件
            my_pl4 = pA.pl4_Analysis(self.filename)             #创建pl4对象
            my_pl4.get_ans()                                    #获取结果
            os.remove(self.filename+'.pl4')                     #删除pl4文件
            os.remove(self.filename+'.dbg')
            os.remove(self.filename+'.lis')
            