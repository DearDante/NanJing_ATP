# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:28:37 2018

@author: 43926
"""
import xlwt
import xlrd

class ATP_excel(object):

#初始化excel表，包括第一行超参数，用户关注开关名称

    default_model_size = 5           #只是模式总数的初始量，不用客户设置
    
    def create_excel(self,ATPfile):
        
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1')
        sheet.write(0,0,'仿真重复次数')
        sheet.write(0,1,'开关时间偏差量')
        sheet.write(0,2,'结果标签')
        sheet.write(0,3,'波形提取时间')
        sheet.write(0,4,'取重复结果%')
        sheet.write(0,5,'绝对值')
        sheet.write(0,6,'运行模式')
        
        sheet.write(1,0,10)
        sheet.write(1,1,0.0001)
        sheet.write(1,2,'NaN')
        sheet.write(1,3,'NaN')
        sheet.write(1,4,100)
        sheet.write(1,5,0)
        sheet.write(1,6,0)
        
        sheet.write(2,1,'左节点,右节点')
        
        for i in range(self.default_model_size):
            sheet.write(i+3,0,'model_%.d' % (i+1))
            
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

        self.info = sh.row_values(1)
        self.switch_list = []
        for i in sh.row_values(2):
            if i == '':
                continue
            else:
                self.switch_list.append(i)
#        print(self.switch_list)
        self.model_list = []
        for i in range(3,nrows):
            if(sh.row_values(i)[1] != ''):
#                print(sh.row_values(i))
                self.model_list.append(sh.row_values(i))
            else:
                continue
    #获取第一行的超参数。    
    def get_info(self):
        return self.info
    #获取用户关心的开关列表
    def get_switch_list(self):
        return self.switch_list
    #获取模式列表
    def get_model_list(self):
        return self.model_list

if __name__ == '__main__':
    a = ATP_excel()
    a.read_excel(r'D:\ATPATP\test')