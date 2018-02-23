# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\43926\Desktop\my_Eric\ATP_New\new_project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 156)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 362, 76))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.p_name_lE = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_name_lE.setObjectName("p_name_lE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.p_name_lE)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.p_path_lE = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_path_lE.setObjectName("p_path_lE")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p_path_lE)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.con_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.con_btn.setObjectName("con_btn")
        self.horizontalLayout.addWidget(self.con_btn)
        self.can_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.can_btn.setObjectName("can_btn")
        self.horizontalLayout.addWidget(self.can_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "项目名称"))
        self.label_2.setText(_translate("Dialog", "项目路径"))
        self.con_btn.setText(_translate("Dialog", "确认"))
        self.can_btn.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

