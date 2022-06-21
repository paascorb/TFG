from PyQt5.QtWidgets import QWidget, QItemDelegate, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets

from LogicaDeNegocio.BooleanFunctionManager import *


class ListarBF(QWidget):
    def __init__(self, parent, menu_bf):
        self.parent = parent
        super().__init__()
        self.menu_bf = menu_bf
        self.bfs = list_boolean_functions()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
        self.setWindowIcon(icon)
        self.setObjectName("Lista de Funciones Booleanas")
        self.resize(750, 450)
        self.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                           "color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.lineEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 4, 1, 1)
        self.toolButton_load = QtWidgets.QToolButton(self)
        self.toolButton_load.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_load.setStyleSheet("QToolButton{\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(71, 71, 71);\n"
                                           "}\n"
                                           "\n"
                                           "QToolButton:hover{\n"
                                           "    background-color: rgb(100, 100, 100);\n"
                                           "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/load.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_load.setIcon(icon)
        self.toolButton_load.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_load.setObjectName("toolButton_load")
        self.gridLayout.addWidget(self.toolButton_load, 0, 0, 1, 1)
        self.toolButton_Return = QtWidgets.QToolButton(self)
        self.toolButton_Return.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_Return.setStyleSheet("QToolButton{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(71, 71, 71);\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "    background-color: rgb(100, 100, 100);\n"
                                      "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/return.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_Return.setIcon(icon1)
        self.toolButton_Return.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_Return.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton_Return, 0, 5, 1, 1)
        self.tableBF = QtWidgets.QTableWidget(self)
        self.tableBF.setMinimumSize(QtCore.QSize(725, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableBF.setFont(font)
        self.tableBF.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(177, 177, 177);")
        self.tableBF.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableBF.setAlternatingRowColors(True)
        self.tableBF.setObjectName("tableBF")
        self.tableBF.setColumnCount(4)
        self.tableBF.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableBF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableBF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableBF.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableBF.setHorizontalHeaderItem(3, item)
        self.tableBF.horizontalHeader().setCascadingSectionResizes(False)
        self.tableBF.horizontalHeader().setDefaultSectionSize(100)
        self.tableBF.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableBF, 1, 0, 1, 6)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.toolButton_remove = QtWidgets.QToolButton(self)
        self.toolButton_remove.setMinimumSize(QtCore.QSize(40, 40))
        self.toolButton_remove.setStyleSheet("QToolButton{\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(71, 71, 71);\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:hover{\n"
                                             "    background-color: rgb(100, 100, 100);\n"
                                             "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/remove.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_remove.setIcon(icon2)
        self.toolButton_remove.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_remove.setObjectName("toolButton_remove")
        self.gridLayout.addWidget(self.toolButton_remove, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        header = self.tableBF.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.tableBF.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.add_bfs_to_table(self.bfs)

        self.toolButton_Return.clicked.connect(self.close)
        self.toolButton_remove.clicked.connect(self.remove_row)
        self.toolButton_load.clicked.connect(self.cargar_bf)

        self.tableBF.horizontalHeader().sectionClicked.connect(self.sort_by_column)
        self.tableBF.horizontalHeader().sectionDoubleClicked.connect(self.invert_sort_by_column)
        self.lineEdit.textChanged.connect(self.create_table_by_search)
        self.tableBF.itemDoubleClicked.connect(self.cargar_bf)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Lista de Funciones Booleanas"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar"))
        self.toolButton_load.setText(_translate("Form", "..."))
        self.toolButton_Return.setText(_translate("Form", "..."))
        item = self.tableBF.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableBF.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Número Variables"))
        item = self.tableBF.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Salidas"))
        item = self.tableBF.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Monótona"))
        self.label.setText(_translate("Form", "Selecciona la función que deseas cargar:"))
        self.toolButton_remove.setText(_translate("Form", "..."))

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

    def remove_row(self):
        if self.tableBF.rowCount() > 0:
            current_row = self.tableBF.currentRow()
            if current_row != -1:
                bf_id = self.tableBF.item(current_row, 0).text()
                self.tableBF.removeRow(current_row)
                remove_boolean_function(bf_id)

    def add_bfs_to_table(self, bfs):
        for i, bf in enumerate(bfs):
            numRows = self.tableBF.rowCount()
            self.tableBF.insertRow(numRows)
            self.tableBF.setItem(i, 0, QtWidgets.QTableWidgetItem(bf.name))
            self.tableBF.setItem(i, 1, QtWidgets.QTableWidgetItem(str(bf.num_variables)))
            if bf.monotone_flag:
                self.tableBF.setItem(i, 3, QtWidgets.QTableWidgetItem("Sí"))
            else:
                self.tableBF.setItem(i, 3, QtWidgets.QTableWidgetItem("No"))
            if bf.outputs:
                output_str = "("
                for j, elem in enumerate(bf.outputs):
                    output_str = output_str + str(elem)
                    if j != len(bf.outputs) - 1:
                        output_str = output_str + ","
                output_str = output_str + ")"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(output_str)
                text_scrolleable.setReadOnly(True)
                self.tableBF.setCellWidget(i, 2, text_scrolleable)
        self.tableBF.setItemDelegate(AligDelegate())

    def cargar_bf(self):
        row = self.tableBF.currentRow()
        if row != -1:
            bf_name = self.tableBF.item(row, 0).text()
            bf = next(x for x in self.bfs if x.name == bf_name)
            self.menu_bf.show()
            self.menu_bf.set_bf(bf)
            self.parent = self.menu_bf
            self.close()

    def create_table_by_search(self):
        self.tableBF.setRowCount(0)
        crit = self.lineEdit.text()
        if crit:
            bf_crit = [x for x in self.bfs if x.name.lower().startswith(crit.lower())]
            if bf_crit:
                for i, bf in enumerate(bf_crit):
                    numRows = self.tableBF.rowCount()
                    self.tableBF.insertRow(numRows)
                    self.tableBF.setItem(i, 0, QtWidgets.QTableWidgetItem(bf.name))
                    self.tableBF.setItem(i, 1, QtWidgets.QTableWidgetItem(str(bf.num_variables)))
                    if bf.monotone_flag:
                        self.tableBF.setItem(i, 3, QtWidgets.QTableWidgetItem("Sí"))
                    else:
                        self.tableBF.setItem(i, 3, QtWidgets.QTableWidgetItem("No"))
                    if bf.outputs:
                        output_str = "("
                        for j, elem in enumerate(bf.outputs):
                            output_str = output_str + str(elem)
                            if j != len(bf.outputs) - 1:
                                output_str = output_str + ","
                        output_str = output_str + ")"
                        text_scrolleable = QTextEdit()
                        text_scrolleable.setText(output_str)
                        text_scrolleable.setReadOnly(True)
                        self.tableBF.setCellWidget(i, 2, text_scrolleable)
                self.tableBF.setItemDelegate(AligDelegate())
            else:
                self.tableBF.setRowCount(0)
        else:
            self.add_bfs_to_table(self.bfs)

    def sort_by_column(self):
        column = self.tableBF.currentColumn()
        self.tableBF.sortItems(column, QtCore.Qt.AscendingOrder)

    def invert_sort_by_column(self):
        column = self.tableBF.currentColumn()
        self.tableBF.sortItems(column, QtCore.Qt.DescendingOrder)


class AligDelegate(QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QItemDelegate.paint(self, painter, option, index)
