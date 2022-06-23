from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.BooleanFunctionManager import *
from ModeloDeDominio.BooleanFunction import BooleanFunction
from Presentacion.PresentacionAuxiliar import *


class NuevoBF(QWidget):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.close_accepted = False
        self.setObjectName("Crear Función Booleana")
        self.resize(750, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                                    "color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setContentsMargins(100, 40, 100, 20)
        self.gridLayout_2.setHorizontalSpacing(36)
        self.gridLayout_2.setVerticalSpacing(29)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.table_ouputs = QtWidgets.QTableWidget(self)
        self.table_ouputs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_ouputs.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.table_ouputs.setObjectName("table_ouputs")
        self.table_ouputs.setColumnCount(2)
        self.table_ouputs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_ouputs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_ouputs.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.table_ouputs, 3, 0, 3, 2)
        self.text_fb_name = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_fb_name.setFont(font)
        self.text_fb_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_fb_name.setObjectName("text_fb_name")
        self.gridLayout.addWidget(self.text_fb_name, 1, 1, 1, 2)
        self.spin_n_variables = QtWidgets.QSpinBox(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spin_n_variables.setFont(font)
        self.spin_n_variables.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.spin_n_variables.setObjectName("spin_n_variables")
        self.gridLayout.addWidget(self.spin_n_variables, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_1 = QtWidgets.QToolButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_1.sizePolicy().hasHeightForWidth())
        self.toolButton_1.setSizePolicy(sizePolicy)
        self.toolButton_1.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_1.setFont(font)
        self.toolButton_1.setStyleSheet("QToolButton{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(71, 71, 71);;}\n"
                                        "\n"
                                        "QToolButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.toolButton_1.setObjectName("toolButton_1")
        self.verticalLayout.addWidget(self.toolButton_1)
        self.toolButton_0 = QtWidgets.QToolButton(self)
        self.toolButton_0.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_0.setFont(font)
        self.toolButton_0.setStyleSheet("QToolButton{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(71, 71, 71);;}\n"
                                        "\n"
                                        "QToolButton:hover{\n"
                                        "    background-color: rgb(100, 100, 100);\n"
                                        "}")
        self.toolButton_0.setObjectName("toolButton_0")
        self.verticalLayout.addWidget(self.toolButton_0)
        self.gridLayout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 20, -1, 20)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Aceptar = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_Aceptar.sizePolicy().hasHeightForWidth())
        self.pushButton_Aceptar.setSizePolicy(sizePolicy)
        self.pushButton_Aceptar.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_Aceptar.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Aceptar.setFont(font)
        self.pushButton_Aceptar.setStyleSheet("QPushButton{\n"
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
        self.pushButton_Aceptar.setObjectName("pushButton_Aceptar")
        self.horizontalLayout.addWidget(self.pushButton_Aceptar)
        self.pushButton_Cancelar = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancelar.setSizePolicy(sizePolicy)
        self.pushButton_Cancelar.setMinimumSize(QtCore.QSize(150, 25))
        self.pushButton_Cancelar.setMaximumSize(QtCore.QSize(250, 25))
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
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        header = self.table_ouputs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_ouputs.setAlternatingRowColors(True)
        self.table_ouputs.verticalHeader().setVisible(False)
        delegate_one_column = DelegateTableOutputs(self.table_ouputs)
        self.table_ouputs.setItemDelegate(delegate_one_column)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.text_fb_name, self.spin_n_variables)
        self.setTabOrder(self.spin_n_variables, self.toolButton_1)
        self.setTabOrder(self.toolButton_1, self.toolButton_0)
        self.setTabOrder(self.toolButton_0, self.pushButton_Aceptar)
        self.setTabOrder(self.pushButton_Aceptar, self.pushButton_Cancelar)
        self.setTabOrder(self.pushButton_Cancelar, self.table_ouputs)

        self.spin_n_variables.textChanged.connect(self.rellenar_tabla)
        self.pushButton_Cancelar.clicked.connect(self.close)
        self.pushButton_Aceptar.clicked.connect(self.acept_and_save_form)
        self.toolButton_0.clicked.connect(self.put_0_on_focus)
        self.toolButton_1.clicked.connect(self.put_1_on_focus)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form_Nuevo_FB", "Crear Función Booleana"))
        self.label_2.setText(_translate("Form_Nuevo_FB", "Número de variables:"))
        self.label.setText(_translate("Form_Nuevo_FB", "Nombre de la Función Booleana:"))
        item = self.table_ouputs.horizontalHeaderItem(0)
        item.setText(_translate("Form_Nuevo_FB", "Posición"))
        item = self.table_ouputs.horizontalHeaderItem(1)
        item.setText(_translate("Form_Nuevo_FB", "Valor de la salida"))
        self.label_3.setText(_translate("Form_Nuevo_FB", "Creación Función Booleana"))
        self.toolButton_1.setText(_translate("Form_Nuevo_FB", "1"))
        self.toolButton_0.setText(_translate("Form_Nuevo_FB", "0"))
        self.pushButton_Aceptar.setText(_translate("Form_Nuevo_FB", "Aceptar"))
        self.pushButton_Cancelar.setText(_translate("Form_Nuevo_FB", "Cancelar"))

    def acept_and_save_form(self):
        nombre_bf = self.text_fb_name.text()
        if not nombre_bf:
            crear_mensaje_error('Introduzca el nombre de la función booleana', "Función Booleana")
        elif '"' in nombre_bf or ":" in nombre_bf:
            crear_mensaje_error('No intentes romperme el programa', "Un saludo")
            self.text_fb_name.clear()
        else:
            all_bf = list_boolean_functions()
            edit = False
            if any(x for x in all_bf if x.name == nombre_bf):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Question)
                box.setWindowTitle('GUARDAR')
                box.setText('Ya existe una Función Booleana con ese nombre \r\n ¿Deseas sobreescribirla?')
                box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                buttonY = box.button(QtWidgets.QMessageBox.Yes)
                buttonY.setText('Sí')
                buttonN = box.button(QtWidgets.QMessageBox.No)
                buttonN.setText('No')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
                box.setWindowIcon(icon)
                box.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                                  "color: rgb(255, 255, 255);")
                buttonN.setStyleSheet("background-color: rgb(71, 71, 71)")
                buttonY.setStyleSheet("background-color: rgb(71, 71, 71)")
                box.exec_()

                if box.clickedButton() == buttonY:
                    edit = True
                else:
                    return
            outputs = self.get_outputs_from_table()
            bf = BooleanFunction(nombre_bf, int(self.spin_n_variables.text()), outputs)
            bf.set_monotone_flag(Aux.is_monotone(bf.outputs))
            if edit:
                edit_boolean_function(bf)
            else:
                add_boolean_function(bf)
            self.close_accepted = True
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.close()

    def rellenar_tabla(self):
        self.table_ouputs.setRowCount(0)
        num = int(self.spin_n_variables.text())
        for i in range(2**num):
            numRows = self.table_ouputs.rowCount()
            self.table_ouputs.insertRow(numRows)
            self.table_ouputs.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
            self.table_ouputs.setItem(i, 1, QtWidgets.QTableWidgetItem('0'))

    def get_outputs_from_table(self):
        outputs = list()
        for row in range(self.table_ouputs.rowCount()):
            item = self.table_ouputs.item(row, 1)
            outputs.append(int(item.text()))
        return outputs

    def put_0_on_focus(self):
        row = self.table_ouputs.currentRow()
        self.table_ouputs.setItem(row, 1, QtWidgets.QTableWidgetItem('0'))
        current = self.table_ouputs.currentIndex()
        next_index = current.sibling(row + 1, current.column())
        if next_index.isValid():
            self.table_ouputs.setCurrentIndex(next_index)
            self.table_ouputs.edit(next_index)

    def put_1_on_focus(self):
        row = self.table_ouputs.currentRow()
        self.table_ouputs.setItem(row, 1, QtWidgets.QTableWidgetItem('1'))
        current = self.table_ouputs.currentIndex()
        next_index = current.sibling(row + 1, current.column())
        if next_index.isValid():
            self.table_ouputs.setCurrentIndex(next_index)
            self.table_ouputs.edit(next_index)

    def closeEvent(self, event):
        if self.close_accepted:
            self.parent.show()
            event.accept()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('SALIR')
            box.setText('¿Estás seguro que deseas cancelar?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Sí')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('No')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
            box.setWindowIcon(icon)
            box.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                              "color: rgb(255, 255, 255);")
            buttonN.setStyleSheet("background-color: rgb(71, 71, 71)")
            buttonY.setStyleSheet("background-color: rgb(71, 71, 71)")
            box.exec_()

            if box.clickedButton() == buttonY:
                self.parent.show()
                event.accept()
            else:
                event.ignore()
