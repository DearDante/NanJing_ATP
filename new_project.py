# -*- coding: utf-8 -*-

"""
Module implementing New_Project.
"""

from PyQt5.QtCore import pyqtSlot,QCoreApplication
from PyQt5.QtWidgets import QDialog

from Ui_new_project import Ui_Dialog
import ATP_excel as Ae

class New_Project(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(New_Project, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_con_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        a = self.p_path_lE.text().split('\\')
        a.append(self.p_name_lE.text())
        b = '\ '.join(a)
        c = b.split()
        self.run_path = ''.join(c)
        self.my_excel = Ae.ATP_excel()
        self.my_excel.create_excel(self.run_path)
        self.destroy()
        
    def get_path(self):
        return self.run_path
    
    @pyqtSlot()
    def on_can_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.destroy()
