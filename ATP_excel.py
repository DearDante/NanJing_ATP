# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:28:37 2018

@author: 43926
"""
import xlwt
import xlrd

class ATP_excel(object):

#初始化excel表，包括第一行超参数，用户关注开关名称

    default_model_size = 15
    
    def create_excel(self,times,delta,switch_list,ATPfile):
        
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1')
        sheet.write(0,0,'仿真重复次数=%.d' % times)
        print (delta)
        sheet.write(0,1,'开关时间偏差量=%f' % delta)
        print('开关时间偏差量=%f' % delta)
        n = 1
        for i in switch_list:
            sheet.write(1,n,i)
            n = n+1
        
        for i in range(self.default_model_size):
            sheet.write(i+2,0,'model_%.d' % (i+1))
            
        wbk.save(ATPfile + '.xls')
          
    def read_excel(self,ATPfile):              #读取模式信息，返回模式列表。
        #工作表存放地址
        fname = ATPfile + '.xls'
        #打开工作表
        bk = xlrd.open_workbook(fname)
        
        try:
            sh = bk.sheet_by_name("Sheet1")
        except:
            print('No sheet in %s named Sheet1',format(fname))
            
        nrows = sh.nrows
        #ncols = sh.ncols

        self.info = sh.row_values(0)
        self.switch_list = sh.row_values(1)
        self.model_list = []
        for i in range(2,nrows):
            if(sh.row_values(i)[1] != ''):
                self.model_list.append(sh.row_values(i))
            else:
                continue
    #获取第一行的超参数。    
    def get_info(self):
        args_list = []
        for i in self.info:
            if(i != ''):
                data = float(i.split('=')[-1])
                args_list.append(data)
            else:
                continue
        return args_list
    #获取用户关心的开关列表
    def get_switch_list(self):
        return self.switch_list
    #获取模式列表
    def get_model_list(self):
        return self.model_list
        