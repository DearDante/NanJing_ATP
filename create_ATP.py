# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:48:32 2018
完成原始ATP文件的读取
完成模型的读取
完成新ATP文件的生成
@author: 43926
"""
import Series_Template as ST
import re
import ATP_model as am
class create_ATP(object):
    
    def __init__(self,ATPfile):
        self.__source = []
        self.filename = ATPfile
        self.__file = open(self.filename+'.atp','r')
        for i in self.__file.readlines():
            self.__source.append(i)
        self.__file.close()
        
    #获取开关字段；获取Tmax
    def get_info(self):
        self.switch_end = 0
        self.switch_start = 0
        self.Tmax_index = 0
        for i in self.__source:
            if i == '/SWITCH\n':
                self.switch_start = self.__source.index(i)+2    #获取switch在列表中的起始位置
            elif i == '/SOURCE\n':
                self.switch_end = self.__source.index(i)      #获取switch在列表中的结束位置
            elif i == 'C  dT  >< Tmax >< Xopt >< Copt ><Epsiln>\n':
                self.Tmax_index = self.__source.index(i)
            else:
                continue   
    def get_Tmax(self):
        sor = float(self.__source[self.Tmax_index+1].split()[1])
        return sor

    #识别开关字段中，包含用户选择的开关pat的字符串索引号。
    def choose_switch(self,pat):
        switch_index = []
        for i in range(self.switch_start,self.switch_end):
            m = re.match('  '+pat,self.__source[i])
            if m is not None:
                switch_index.append(i)
            else:
                continue
        return switch_index
    
    #同相开关的偏差处理,delta为偏差量
    def deal(self,p_str,delta):
        a = p_str[1:-1].split(',')
        a_1 = float(a[0]) + delta
        a_2 = float(a[1]) - delta
        b = '[%f,%f]' % (a_1,a_2)
        return b
    
    #将客户选择的模式转换为switch下的字符串，并进行替换。delta为偏差量。
    def set_ATP(self,model,delta):                       
        #model为excel中提取出来的策略总表，元素为单个策略列表
        for i in range(len(model)):
            #对每一个策略进行分解，转化为四个元素
            pat = model[i][0]+'.{0,5}'+model[i][1]+'.*'
            s_index = self.choose_switch(pat)
            for j in range(len(s_index)):
                #解决由于编码差异导致的字符串长度变化
                sor_str = re.match('  '+pat,self.__source[s_index[j]]).group()
                my_len = len(sor_str)-66
                name = re.match('  '+pat,self.__source[s_index[j]]).group()[:my_len]
                #处理区间量
                if type(model[i][2]) == str:
                    a = self.deal(model[i][2],delta)
                    t_start = ST.Series_Template(a).distribute()[0]
                    if type(model[i][3]) == str:
                        b = self.deal(model[i][3],delta)
                        t_end = ST.Series_Template(b).distribute()[0]
                    else:
                        t_end = float(model[i][3])
                else:
                    t_start = float(model[i][2])
                    if type(model[i][3]) == str:
                        a = self.deal(model[i][3],delta)
                        t_end = ST.Series_Template(a).distribute()[0]
                    else:
                        t_end = float(model[i][3])
                #将四个元素合并为符合ATP'  %-6s%-6s%10f%10f                                             0\n)
#                a = input('稍等')
                model_str = name + '%10f%10f                                             0\n' % (t_start,t_end)
#                print(model_str)
                self.__source[s_index[j]] = model_str
    
   
    
    def generate(self,n):                           #生成新atp文件
        new_file = open(self.filename+'_%.d' % (n+1) +'.atp' ,'w')
        for i in self.__source:
            new_file.writelines(i)
        new_file.close()
            
if __name__ == '__main__':
    a = create_ATP(r'C:\Users\43926\Desktop\haha')   
    a.get_info()
    b=a.get_Tmax()
    a.choose_switch('XM.')
    a.deal('[1.2,1.3]',0.0001)
    
    c = am.ATP_model()
    c.set_model(r"C:\Users\43926\Desktop\haha")
    d = c.get_model()
    
    a.set_ATP(d[0],0.0001)
    a.generate(1)