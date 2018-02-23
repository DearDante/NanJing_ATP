# -*- coding: utf-8 -*-

"""
Module implementing New_ATP_Main.
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_ATP_Window import Ui_MainWindow

import create_ATP as cATP
import ATP_excel as Ae
import ATP_model as Am
import run_ATP as rATP
import pl4_Analysis as pA
import os


class New_ATP_Main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(New_ATP_Main, self).__init__(parent)
        self.setupUi(self)
    
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
        raise NotImplementedError
    
    @pyqtSlot()
    def on_r_excel_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cB_model_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_all_model_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if(self.all_model.isChecked()):
            self.scrollArea.setEnabled(False)
        else:
            self.scrollArea.setEnabled(True)
    
    @pyqtSlot()
    def on_default_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_run_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_cancel_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = New_ATP_Main()
    mywin.show()
    sys.exit(app.exec_())
