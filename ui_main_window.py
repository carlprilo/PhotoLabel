# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self,num,content):
        # call QWidget constructor
        super().__init__()
        self.boxList = []
        self.cameraNum = num
        self.imageLabelList = []
        self.verLayoutList = []
        self.boxContent = content
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        self.save_bt = QtWidgets.QPushButton(Form)
        self.save_bt.setObjectName("save_bt")
        self.verticalLayout.addWidget(self.save_bt)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        
        for i in range (self.cameraNum):
            verticalLayout = QtWidgets.QVBoxLayout()
            verticalLayout.setObjectName("%s%d"%("verticalLayout",i))
            image_label = QtWidgets.QLabel(Form)
            image_label.setObjectName("%s%d"%("image_label",i))
            verticalLayout.addWidget(image_label)
            dirs_box = QtWidgets.QComboBox(Form)
            dirs_box.setObjectName("%s%d"%("dirs_box",i))
            self.initBox(dirs_box)
            verticalLayout.addWidget(dirs_box)
            self.horizontalLayout.addLayout(verticalLayout)
            self.verLayoutList.append(verticalLayout)
            self.imageLabelList.append(image_label)
            self.boxList.append(dirs_box)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.save_bt.setText(_translate("Form","Save"))
        for image_label  in self.imageLabelList:
            image_label.setText(_translate("Form", "Camera"))

    def initBox(self,box):
        for i in self.boxContent:
            box.addItem(i)
