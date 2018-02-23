# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:20:38 2018

@author: 43926
"""

import struct
import binascii
import pandas
import os
class pl4_Analysis(object):
    

    def __init__(self,ATPfile):
        self.__file = open(ATPfile+'.pl4','rb')
        a = struct.iter_unpack('c',self.__file.read())                    
        self.__file.close()
        self.__b = []
        for i in a:
            self.__b.append(i[0])
        
        
    
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
            
    def __Analysis(self,start_time,end_time):
        self.__prepare()
        self.__get_point()
        self.my_ans = pandas.DataFrame()
        self.start_t = 0
        self.end_t = 0
        for i in range(0,self.total_num+1):
            ans = []
            count = 0
            for j in range(self.start-1,self.fin-1,4*(self.total_num+1)):
                ans.append(self.b2any('f',self.__b[j+i:j+i+4],4))
                #根据用户选择的起止时间，来标定数据中对应的时间区间起止点
                if i == 0:
#                    print(self.b2any('f',self.__b[j+i:j+i+4],4))
                    if(self.b2any('f',self.__b[j+i:j+i+4],4) < start_time):
                        self.start_t = count
                    elif(self.b2any('f',self.__b[j+i:j+i+4],4) < end_time):
                        self.end_t = count+1
                    count = count + 1
            if(i == 0):
                self.my_ans.insert(i,'time',ans)
            else:
                self.my_ans.insert(i,self.mymodel[i-1].strip(),ans)
    
    def get(self):
        return self.my_ans
                
    def get_ans(self,filename,ans_info,num,model_num):
        self.__Analysis(ans_info[1],ans_info[2])
        #不同的模式结果记录在不同的文件中
        filename = filename+'_%d.txt' % model_num
        self.ans_file = open(filename,'a+')
#        print(ans_info[3].split(','))
#        print(self.my_ans[ans_info[3].split(',')])
        if (ans_info[3] != 'NAN') & (ans_info[3] != ''):
            self.my_ans_2 = self.my_ans[ans_info[3].split(',')][self.start_t:self.end_t]#存放用户需要的时间段及结果标签对应的数据
        else:
            self.my_ans_2 = self.my_ans.iloc[self.start_t:self.end_t,1:]
#        print(self.my_ans_2.shape)
        if ans_info[0]:
            a = abs(self.my_ans_2.max())
        else:
            a = self.my_ans_2.max()
            
        if os.path.getsize(self.ans_file.name) < 1:
            self.ans_file.write('      ')
            for i in range(len(a)):
                self.ans_file.write('%12s ' % self.my_ans_2.max().index[i].strip())
            self.ans_file.write('\n')
        self.ans_file.write('%-6d' % (num+1))
        for i in range(len(a)):
            self.ans_file.write('%10e '% self.my_ans_2.max()[i])
        self.ans_file.write('\n')
        self.ans_file.close()
        
        
        
if __name__ == '__main__':
    a = pl4_Analysis(r'D:\ATPATP\test_1')