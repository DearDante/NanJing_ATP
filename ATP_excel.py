# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:28:37 2018

@author: 43926
"""
import win32com.client as win32
class ATP_excel(object):

#初始化excel表，包括第一行超参数，用户关注开关名称

    default_model_size = 15
    
    def __init__(self,times,delta,switch_list):
        self.x1 = win32.gencache.EnsureDispatch('Excel.Application')
        self.ss = self.x1.Workbooks.Add()
        self.sh = self.ss.ActiveSheet
        self.x1.Visible = True
        
        self.sh.Cells(1,1).Value = '仿真重复次数=%.d' % times
        self.sh.Cells(1,2).Value = '开关时间偏差量=%.d' % delta
        n = 2
        for i in switch_list:
            self.sh.Cells(2,n).Value = i
            n = n+1
        
        for i in range(self.default_model_size):
            self.sh.Cells(i+3,1).Value = 'model_%.d' % (i+1)
            
    def read_excel(self):              #读取模式信息，返回模式列表。
        pass
        
        