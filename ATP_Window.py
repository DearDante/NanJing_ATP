# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from Ui_ATP_Window import Ui_MainWindow
import new_project
import create_ATP as cATP
import ATP_excel as Ae
import ATP_model as Am
import run_ATP as rATP
import pl4_Analysis as pA
import os
import subprocess

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.plotpath = r'C:\ATP\PlotXY\PlotXY.exe'
        
    @pyqtSlot()
    def on_abs_cb_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.abs_cb.isChecked():
            self.abs = False
        else:
            self.abs = True
    
    @pyqtSlot()
    def on_g_excel_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dlg = new_project.New_Project(self)
        dlg.show()
        self.filename = dlg.get_path()
    
    @pyqtSlot()
    def on_r_excel_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        files, n_1 = QFileDialog.getOpenFileName(self,"选取文件",r"C:/",'Text Files(*.xls)')
        self.filename = files.split('.')[0]
        self.my_excel = Ae.ATP_excel()
        self.my_excel.read_excel(self.filename)
        self.info = self.my_excel.get_info()
        self.run_times = self.info[0]
        self.delta = self.info[1]
        self.result = self.info[2]
        self.percent = self.info[3]
        self.abs = self.info[4]
        self.run_model = self.info[5]
        
        self.times_le.setText(str(self.run_times))
        a = Am.ATP_model()
        a.set_model(self.filename)
        self.model_list = a.get_model()
#        print(self.model_list)
    
    @pyqtSlot()
    def on_cB_model_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 1
    
    @pyqtSlot()
    def on_cB_model_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 2
    
    @pyqtSlot()
    def on_cB_model_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 3
    
    @pyqtSlot()
    def on_cB_model_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 4
    
    @pyqtSlot()
    def on_cB_model_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 5
    
    @pyqtSlot()
    def on_cB_model_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 6
    
    @pyqtSlot()
    def on_cB_model_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 7
    
    @pyqtSlot()
    def on_cB_model_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.runmodel = 8
    
    @pyqtSlot()
    def on_all_model_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if(self.all_model.isChecked()):
            self.scrollArea.setEnabled(False)
            self.runmodel = 0
        else:
            self.scrollArea.setEnabled(True)
    
    @pyqtSlot()
    def on_default_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.run_times = 1
        self.delta = 0.0001
        self.result = 'NaN'
        self.percent = 100
        self.abs = 0
        self.run_model = 0
    
    @pyqtSlot()
    def on_run_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.__ori_atp = cATP.create_ATP(self.filename)
        self.run_times = float(self.times_le.text())
        try:
            self.ans_times_start = float(self.time_start_lE.text())
        except:
            self.ans_times_start = 0
        
        try:
            self.ans_times_end = float(self.time_end_lE.text())
        except:
            self.ans_times_end = 99999.9
            
        try:
            self.ans_tips = self.result_tE.toPlainText()
        except:
            self.ans_tips = 'NAN'
        
        #成果信息，绝对值，起止时间，结果标签
        self.ans_info = [self.abs,self.ans_times_start,self.ans_times_end,self.ans_tips]
        
        print(self.ans_info)
        for j in self.model_list:
            for i in range(int(self.run_times)):
                self.__ori_atp.get_info()
                '''
                print(self.run_times)
#                if self.times_le.read()
                print(self.delta)
                print(self.result)
                print(self.percent)
                print(self.abs)
                print(self.run_model)
                print(j)'''
                self.__ori_atp.set_ATP(j,self.delta)                #设置新的开关协议
                self.__ori_atp.generate(i)                          #生成新的atp文件
                #if i == 0:
                #    ppath = self.run_path
                #else:
                
                
                ppath = self.filename+'_%d' % (i+1)
                rATP.run_ATP(ppath)                         #生成pl4文件    
                my_pl4 = pA.pl4_Analysis(ppath)             #创建pl4对象
                my_pl4.get_ans(self.filename,self.ans_info,i,self.model_list.index(j))                                    #获取结果
                #如果运行次数为1，则进入调试模式，保留Pl4文件，调用plotXY。
                if self.run_times == 1:
                    subprocess.Popen(self.plotpath + ' ' + ppath+'.pl4')
                else:
                    os.remove(ppath+'.pl4')                     #删除pl4文件
                os.remove(ppath+'.dbg')
                os.remove(ppath+'.lis')
    @pyqtSlot()
    def on_cancel_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        reply = QMessageBox.question(self, '信息', '确认退出吗？', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.destroy()
        else:
            pass
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '信息', '确认退出吗？', 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ != '__main__':
    app = QApplication(sys.argv)
    mywin = MainWindow()
    mywin.show()
    sys.exit(app.exec_())
