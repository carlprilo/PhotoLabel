# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout0 = QtWidgets.QVBoxLayout()
        self.verticalLayout0.setObjectName("verticalLayout0")
        self.image_label0 = QtWidgets.QLabel(Form)
        self.image_label0.setObjectName("image_label0")
        self.verticalLayout0.addWidget(self.image_label0)
        self.dirs_box0 = QtWidgets.QComboBox(Form)
        self.dirs_box0.setObjectName("dirs_box0")
        self.verticalLayout0.addWidget(self.dirs_box0)
        self.initBox(self.dirs_box0)
        self.horizontalLayout.addLayout(self.verticalLayout0)
        self.verticalLayout1 = QtWidgets.QVBoxLayout()
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.image_label1 = QtWidgets.QLabel(Form)
        self.image_label1.setObjectName("image_label1")
        self.verticalLayout1.addWidget(self.image_label1)
        self.dirs_box1 = QtWidgets.QComboBox(Form)
        self.dirs_box1.setObjectName("dirs_box1")
        self.initBox(self.dirs_box1)
        self.verticalLayout1.addWidget(self.dirs_box1)
        self.horizontalLayout.addLayout(self.verticalLayout1)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.image_label2 = QtWidgets.QLabel(Form)
        self.image_label2.setObjectName("image_label2")
        self.verticalLayout2.addWidget(self.image_label2)
        self.dirs_box2 = QtWidgets.QComboBox(Form)
        self.dirs_box2.setObjectName("dirs_box2")
        self.initBox(self.dirs_box2)
        self.verticalLayout2.addWidget(self.dirs_box2)
        self.horizontalLayout.addLayout(self.verticalLayout2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.image_label0.setText(_translate("Form", "TextLabel"))

        self.image_label1.setText(_translate("Form", "TextLabel"))

        self.image_label2.setText(_translate("Form", "TextLabel"))


    def initBox(self,box):
        box.addItem("normal")
        box.addItem("abnormal1")
        box.addItem("abnormal2")


