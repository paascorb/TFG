# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prueba_CamposV.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 450)
        Form.setStyleSheet("QWidget{\n"
"background-image: url(:/images/fondo.png);\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, 15, 40, 15)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Guardar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_Guardar.sizePolicy().hasHeightForWidth())
        self.pushButton_Guardar.setSizePolicy(sizePolicy)
        self.pushButton_Guardar.setMinimumSize(QtCore.QSize(150, 25))
        self.pushButton_Guardar.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Guardar.setFont(font)
        self.pushButton_Guardar.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 71, 71);\n"
"border: 1px solid;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"")
        self.pushButton_Guardar.setAutoDefault(False)
        self.pushButton_Guardar.setDefault(False)
        self.pushButton_Guardar.setFlat(False)
        self.pushButton_Guardar.setObjectName("pushButton_Guardar")
        self.gridLayout.addWidget(self.pushButton_Guardar, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 290, 318))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 0, 0, 2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 2, 1)
        self.pushButton_Cancelar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancelar.setSizePolicy(sizePolicy)
        self.pushButton_Cancelar.setMinimumSize(QtCore.QSize(150, 25))
        self.pushButton_Cancelar.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 71, 71);\n"
"border: 1px solid;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_Cancelar.setObjectName("pushButton_Cancelar")
        self.gridLayout.addWidget(self.pushButton_Cancelar, 3, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_vf_name = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_vf_name.setFont(font)
        self.line_vf_name.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(177, 177, 177);")
        self.line_vf_name.setObjectName("line_vf_name")
        self.horizontalLayout_3.addWidget(self.line_vf_name)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.tablePairs = QtWidgets.QTableWidget(Form)
        self.tablePairs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tablePairs.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(177, 177, 177);")
        self.tablePairs.setObjectName("tablePairs")
        self.tablePairs.setColumnCount(2)
        self.tablePairs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablePairs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tablePairs.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tablePairs, 1, 1, 1, 2)
        self.pushButton_Anadir = QtWidgets.QPushButton(Form)
        self.pushButton_Anadir.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Anadir.setFont(font)
        self.pushButton_Anadir.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 71, 71);\n"
"border: 1px solid;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_Anadir.setObjectName("pushButton_Anadir")
        self.gridLayout.addWidget(self.pushButton_Anadir, 2, 1, 1, 2)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Guardar.setText(_translate("Form", "Guardar"))
        self.label_3.setText(_translate("Form", "Creación manual de un campo de vectores"))
        self.pushButton_Cancelar.setText(_translate("Form", "Cancelar"))
        self.label_2.setText(_translate("Form", "Nombre:"))
        item = self.tablePairs.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sigma"))
        item = self.tablePairs.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tau"))
        self.pushButton_Anadir.setText(_translate("Form", "Añadir"))