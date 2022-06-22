from PyQt5.QtWidgets import QWidget, QItemDelegate, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets

from LogicaDeNegocio.SimplicialComplexManager import *


class ListarSC(QWidget):
    def __init__(self, parent, menu_sc):
        self.parent = parent
        super().__init__()
        self.menu_sc = menu_sc
        self.setObjectName("Lista de Complejos Simpliciales")
        self.resize(750, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                           "color: rgb(255, 255, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
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
        icon.addPixmap(QtGui.QPixmap("../Recursos/load.ico"))
        self.toolButton_load.setIcon(icon)
        self.toolButton_load.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_load.setObjectName("toolButton_load")
        self.gridLayout.addWidget(self.toolButton_load, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 4, 1, 1)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Recursos/remove.ico"))
        self.toolButton_remove.setIcon(icon1)
        self.toolButton_remove.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_remove.setObjectName("toolButton_remove")
        self.gridLayout.addWidget(self.toolButton_remove, 0, 1, 1, 1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/return.ico"))
        self.toolButton_Return.setIcon(icon2)
        self.toolButton_Return.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_Return.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton_Return, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.tableSC = QtWidgets.QTableWidget(self)
        self.tableSC.setMinimumSize(QtCore.QSize(725, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableSC.setFont(font)
        self.tableSC.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(177, 177, 177);")
        self.tableSC.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableSC.setAlternatingRowColors(True)
        self.tableSC.setObjectName("tableSC")
        self.tableSC.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableSC.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableSC.setHorizontalHeaderItem(5, item)
        self.tableSC.horizontalHeader().setCascadingSectionResizes(False)
        self.tableSC.horizontalHeader().setDefaultSectionSize(100)
        self.tableSC.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableSC, 1, 0, 1, 6)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        header = self.tableSC.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        self.tableSC.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        scomplexes = list_simplicial_complexes()
        self.scs = scomplexes
        self.add_scs_to_table(scomplexes)

        self.toolButton_remove.clicked.connect(self.remove_row)
        self.toolButton_Return.clicked.connect(self.close)
        self.toolButton_load.clicked.connect(self.cargar_sc)

        self.tableSC.horizontalHeader().sectionClicked.connect(self.sort_by_column)
        self.tableSC.horizontalHeader().sectionDoubleClicked.connect(self.invert_sort_by_column)
        self.lineEdit.textChanged.connect(self.create_table_by_search)
        self.tableSC.itemDoubleClicked.connect(self.cargar_sc)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Lista de Complejos Simpliciales"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar"))
        self.label.setText(_translate("Form", "Selecciona el complejo simplicial que deseas cargar:"))
        self.toolButton_load.setText(_translate("Form", "..."))
        self.toolButton_remove.setText(_translate("Form", "..."))
        self.toolButton_Return.setText(_translate("Form", "..."))
        item = self.tableSC.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableSC.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ω"))
        item = self.tableSC.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Dimensión"))
        item = self.tableSC.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Característica de Euler"))
        item = self.tableSC.horizontalHeaderItem(4)
        item.setText(_translate("Form", "C-Vector"))
        item = self.tableSC.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Nº Símplices"))

    def remove_row(self):
        if self.tableSC.rowCount() > 0:
            current_row = self.tableSC.currentRow()
            sc_id = self.tableSC.item(current_row, 0).text()
            self.tableSC.removeRow(current_row)
            remove_simplicial_complex(sc_id)

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

    def add_scs_to_table(self, scs):
        for i, sc in enumerate(scs):
            numRows = self.tableSC.rowCount()
            self.tableSC.insertRow(numRows)
            self.tableSC.setItem(i, 0, QtWidgets.QTableWidgetItem(sc.name))
            self.tableSC.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sc.omega)))
            self.tableSC.setItem(i, 2, QtWidgets.QTableWidgetItem(str(sc.dimension)))
            self.tableSC.setItem(i, 3, QtWidgets.QTableWidgetItem(str(int(sc.euler_char))))
            c_vector_str = "("
            for j, elem in enumerate(sc.c_vector):
                c_vector_str = c_vector_str + str(elem)
                if j != len(sc.c_vector) - 1:
                    c_vector_str = c_vector_str + ","
            c_vector_str = c_vector_str + ")"
            self.tableSC.setItem(i, 4, QtWidgets.QTableWidgetItem(c_vector_str))
            self.tableSC.setItem(i, 5, QtWidgets.QTableWidgetItem(str(len(sc.simplex))))
        self.tableSC.setItemDelegate(AligDelegate())

    def cargar_sc(self):
        row = self.tableSC.currentRow()
        if row != -1:
            sc_name = self.tableSC.item(row, 0).text()
            sc = next(x for x in self.scs if x.name == sc_name)
            self.menu_sc.show()
            self.menu_sc.set_sc(sc)
            self.parent = self.menu_sc
            self.close()

    def create_table_by_search(self):
        self.tableSC.setRowCount(0)
        crit = self.lineEdit.text()
        if crit:
            scomplexes = list_simplicial_complexes()
            sc_crit = [x for x in scomplexes if x.name.lower().startswith(crit.lower())]
            if sc_crit:
                for i, sc in enumerate(sc_crit):
                    numRows = self.tableSC.rowCount()
                    self.tableSC.insertRow(numRows)
                    self.tableSC.setItem(i, 0, QtWidgets.QTableWidgetItem(sc.name))
                    self.tableSC.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sc.omega)))
                    self.tableSC.setItem(i, 2, QtWidgets.QTableWidgetItem(str(sc.dimension)))
                    self.tableSC.setItem(i, 3, QtWidgets.QTableWidgetItem(str(int(sc.euler_char))))
                    c_vector_str = "("
                    for j, elem in enumerate(sc.c_vector):
                        c_vector_str = c_vector_str + str(elem)
                        if j != len(sc.c_vector) - 1:
                            c_vector_str = c_vector_str + ","
                    c_vector_str = c_vector_str + ")"
                    self.tableSC.setItem(i, 4, QtWidgets.QTableWidgetItem(c_vector_str))
                    self.tableSC.setItem(i, 5, QtWidgets.QTableWidgetItem(str(len(sc.simplex))))
                self.tableSC.setItemDelegate(AligDelegate())
            else:
                self.tableSC.setRowCount(0)
        else:
            self.add_scs_to_table(list_simplicial_complexes())

    def sort_by_column(self):
        column = self.tableSC.currentColumn()
        self.tableSC.sortItems(column, QtCore.Qt.AscendingOrder)

    def invert_sort_by_column(self):
        column = self.tableSC.currentColumn()
        self.tableSC.sortItems(column, QtCore.Qt.DescendingOrder)


class AligDelegate(QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QItemDelegate.paint(self, painter, option, index)
