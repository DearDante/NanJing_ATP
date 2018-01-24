# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:20:38 2018

@author: 43926
"""

import struct
import binascii
import pandas

class pl4_Analysis(object):
    

    def __init__(self,filename):
        self.__file = open(filename,'rb')
        a = struct.iter_unpack('c',self.__file.read())                    
        self.__file.close()
        self.__b = []
        for i in a:
            self.__b.append(i[0])
        self.__Analysis()
        
    
    def b2any(self,goal_type,sor,num):
        model = None
        for i in range(num):
            if i == 0:
                model = sor[i]
            else:
                model = model + sor[i]
        ans = struct.unpack(goal_type,model)[0]
        return ans

    
    def __prepare(self):
        self.time = self.b2any('19s',self.__b[:19],19)                              #时间
        self.point_num = int(self.b2any('I',self.__b[19:23],4))                     #存储节点总数
        self.vol_num = int(self.b2any('I',self.__b[23:27],4)/2)                     #显示电压数
        self.total_num = int(self.b2any('I',self.__b[27:31],4)/2)                   #总显示数
        self.tacs_num = int(self.b2any('I',self.__b[31:35],4))                      #TACS节点数
        self.start = self.b2any('I',self.__b[39:43],4)                              #数据块其实位置
        self.fin = self.b2any('I',self.__b[43:47],4)                                #数据块结束位置
        
    def __get_point(self):
        sor_info_1 = self.__b[47+self.tacs_num*6:47+self.tacs_num*6+self.point_num*6]
        self.all_point_name = []#所有的节点名称
        for i in range(0,len(sor_info_1),6):
            self.all_point_name.append(str(self.b2any('6s',sor_info_1[i:i+6],6),encoding = 'gbk'))
        
        sor_info_2 = self.__b[47+self.tacs_num*6+self.point_num*6:
            47+self.tacs_num*6+self.point_num*6+self.total_num*8]
        self.model_point = []#电压电流点的索引
        for i in range(0,len(sor_info_2),8):
            self.model_point.append(self.b2any('I',sor_info_2[i:i+4],4))
#        print(self.model_point)    
        self.mymodel = []#模型中的节点名称列表
        for i in range(0,self.total_num):
            self.mymodel.append(self.all_point_name[self.model_point[i]-1])
#        print(self.mymodel) 
            
    def __Analysis(self):
        self.__prepare()
        self.__get_point()
        self.my_ans = pandas.DataFrame()
        for i in range(0,self.total_num+1):
            ans = []
            for j in range(self.start-1,self.fin-1,4*(self.total_num+1)):
                ans.append(self.b2any('f',self.__b[j+i:j+i+4],4))
            if(i == 0):
                self.my_ans.insert(i,'time',ans)
            else:
                self.my_ans.insert(i,self.mymodel[i-1],ans)
                
    def get_ans(self):
        return self.my_ans
            
        
        
        
        
