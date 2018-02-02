# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 02:16:40 2018

@author: 43926
"""

import ATP_excel as ae

class ATP_model(object):
    
    def set_model(self,ATPfile):
        self.model = []
        #从excel表中提取模式信息,暂时针对3相合一的状况
        self.my_excel = ae.ATP_excel()
        self.my_excel.read_excel(ATPfile)
        self.switch = self.my_excel.get_switch_list()
        self.model_sor = self.my_excel.get_model_list()
        
        #将原始模式信息加工成模式列表
        for i in range(len(self.model_sor)):
            cur_model_list = []
            for j in range(1,len(self.switch)):
                cur_model = []  #每一组开关节点对应的模式元组
                a = self.switch[j].split(',')  #拆分左右节点
                if a[0] == '{GND}':
                    cur_model.append(' ')
                    cur_model.append(a[1])
                elif a[1] == '{GND}':
                    cur_model.append(a[0])
                    cur_model.append(' ')
                else:
                    cur_model.append(a[0])
                    cur_model.append(a[1])
                
                print(self.model_sor[i][j])
                #拆分时间序列，分为三种情况：
                #1.两个时间都是固定时间
                #2.两个时间都是区间
                #3.一个固定一个区间
                b = self.model_sor[i][j].split(',')  
                if len(b) == 2:
                    cur_model.append(float(b[0]))
                    cur_model.append(float(b[1]))
                elif len(b) == 4:
                    cur_model.append(b[0]+','+b[1])
                    cur_model.append(b[2]+','+b[3])
                else:
                    if b[0][0] == '[':
                        cur_model.append(b[0]+','+b[1])
                        cur_model.append(float(b[2]))
                    else:
                        cur_model.append(float(b[0]))
                        cur_model.append(b[1]+','+b[2])
                
                cur_model_list.append(cur_model)  #同一模式形成一个列表
            print('model%d' % i)
            print(cur_model_list)
            self.model.append(cur_model_list)
        
    def get_model(self):
        return self.model
        