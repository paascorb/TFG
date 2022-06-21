from LogicaDeNegocio.SimplicialComplexManager import *
import ModeloDeDominio.Auxiliary as Aux
from ModeloDeDominio.SimplicialComplex import SimplicialComplex
from Presentacion.PresentacionAuxiliar import *


class NuevoSC(QWidget):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        Form.setObjectName("Form")
        Form.resize(750, 450)
        Form.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                           "color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.tableSC = QtWidgets.QTableWidget(Form)
        self.tableSC.setMinimumSize(QtCore.QSize(725, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableSC.setFont(font)
        self.tableSC.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(177, 177, 177);")
        self.tableSC.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableSC.setAlternatingRowColors(True)
        self.tableSC.setObjectName("tableSC")
        self.tableSC.setColumnCount(4)
        self.tableSC.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableSC.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableSC.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableSC.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableSC.setHorizontalHeaderItem(3, item)
        self.tableSC.horizontalHeader().setCascadingSectionResizes(False)
        self.tableSC.horizontalHeader().setDefaultSectionSize(100)
        self.tableSC.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableSC, 1, 0, 1, 4)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton.setStyleSheet("QToolButton{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(71, 71, 71);\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color: rgb(100, 100, 100);\n"
                                      "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/return.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.toolButton_load = QtWidgets.QToolButton(Form)
        self.toolButton_load.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_load.setStyleSheet("QToolButton{\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(71, 71, 71);\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:hover{\n"
                                           "    background-color: rgb(100, 100, 100);\n"
                                           "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_load.setIcon(icon1)
        self.toolButton_load.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_load.setObjectName("toolButton_load")
        self.gridLayout.addWidget(self.toolButton_load, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableSC.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableSC.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Número Variables"))
        item = self.tableSC.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Salidas"))
        item = self.tableSC.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Monótona"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "Selecciona la función que deseas cargar:"))
        self.toolButton_load.setText(_translate("Form", "..."))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar"))