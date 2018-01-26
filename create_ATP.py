# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:48:32 2018
完成原始ATP文件的读取
完成模型的读取
完成新ATP文件的生成
@author: 43926
"""

class create_ATP(object):
    
    def __init__(self,ATPfile):
        self.__source = []
        self.filename = ATPfile
        self.__file = open(self.filename+'.atp','r')
        for i in self.__file.readlines():
            self.__source.append(i)
        self.__file.close()
        
    def get_switch(self):
        self.switch_end = 0
        self.switch_start = 0
        for i in self.__source:
            if i == '/SWITCH\n':
                self.switch_start = self.__source.index(i)+1    #获取switch在列表中的起始位置
            elif i == '/SOURCE\n':
                self.switch_end = self.__source.index(i)      #获取switch在列表中的结束位置
            else:
                continue
    
    def get_model(self,model):                       #将客户选择的模式转换为switch下的字符串
        pass
    
    def set_atp(self):                              #替换原始ATP文件中的switch字段
        #for i in range(self.switch_start,self.switch_end):
        #    self.__source[i] = 'changed\n'
        pass
    
    def generate(self,n):                           #生成新atp文件
        new_file = open(self.filename+'_%.d' % (n+1) +'.atp' ,'w')
        self.get_switch()
        for i in self.__source:
            new_file.writelines(i)
        new_file.close()
            
            