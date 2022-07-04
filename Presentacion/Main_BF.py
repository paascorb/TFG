from PyQt5.QtWidgets import QWidget, QItemDelegate, QMainWindow, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets

from ModeloDeDominio.BooleanFunction import BooleanFunction
from Presentacion.Listar_BF import ListarBF
from Presentacion.Listar_SC import ListarSC
from Presentacion.Nuevo_BF import NuevoBF
from Presentacion.Nuevo_SC import NuevoSC
import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.BooleanFunctionManager import *
from Presentacion.PresentacionAuxiliar import *
from LogicaDeNegocio.SimplicialComplexManager import *
from LogicaDeNegocio.Traductor import *


class MenuBF(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu_sc = None
        self.sc_tra = None
        self.window_listar_bf = None
        self.window_nuevo_bf = None
        self.window_listar_sc = None
        self.window_nuevo_sc = None
        self.bf = None
        self.setObjectName("TFG")
        self.resize(750, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("QWidget{\n"
                          "background-image: url(:/images/fondo.png);\n"
                          "background-color: rgb(27, 27, 27);\n"
                          "color: rgb(255, 255, 255);\n"
                          "}\n"
                          "\n"
                          "QToolBar QToolButton{\n"
                          "color: rgb(255, 255, 255);\n"
                          "background-color:transparent;}\n"
                          "\n"
                          "QToolBar QToolButton:hover{\n"
                          "    background-color: rgb(100, 100, 100);\n"
                          "}\n"
                          "\n"
                          "QToolBar::separator{\n"
                          "    background-color: rgb(208, 208, 208);\n"
                          "    width: 2px;\n"
                          "}\n"
                          "\n"
                          "\n"
                          "QMenuBar::item:selected{\n"
                          "    background-color: rgb(100, 100, 100);\n"
                          "}\n"
                          "\n"
                          "QMenu::item:selected{\n"
                          "    background-color: rgb(100, 100, 100);\n"
                          "}\n"
                          "")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(11)
        self.gridLayout_2.setVerticalSpacing(18)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_fijo = QtWidgets.QGridLayout()
        self.gridLayout_fijo.setContentsMargins(10, -1, 10, 15)
        self.gridLayout_fijo.setHorizontalSpacing(24)
        self.gridLayout_fijo.setVerticalSpacing(15)
        self.gridLayout_fijo.setObjectName("gridLayout_fijo")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_fijo.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_n_variables = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_n_variables.setFont(font)
        self.label_n_variables.setObjectName("label_n_variables")
        self.gridLayout_fijo.addWidget(self.label_n_variables, 1, 1, 1, 1)
        self.label_monotona = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_monotona.setFont(font)
        self.label_monotona.setObjectName("label_monotona")
        self.gridLayout_fijo.addWidget(self.label_monotona, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_fijo.addWidget(self.label, 0, 0, 1, 1)
        self.table_outputs = QtWidgets.QTableWidget(self.centralwidget)
        self.table_outputs.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(177, 177, 177);")
        self.table_outputs.setObjectName("table_outputs")
        self.table_outputs.setColumnCount(2)
        self.table_outputs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_outputs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_outputs.setHorizontalHeaderItem(1, item)
        self.gridLayout_fijo.addWidget(self.table_outputs, 6, 0, 1, 2)
        self.label_nombre_bf = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nombre_bf.setFont(font)
        self.label_nombre_bf.setObjectName("label_nombre_bf")
        self.gridLayout_fijo.addWidget(self.label_nombre_bf, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_fijo.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_fijo.addWidget(self.label_3, 5, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_fijo.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_name_variables = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_variables.setFont(font)
        self.label_name_variables.setObjectName("label_name_variables")
        self.gridLayout_fijo.addWidget(self.label_name_variables, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_fijo)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_dinamico.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 29))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuComplejo_Simplicial = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.menuComplejo_Simplicial.setFont(font)
        self.menuComplejo_Simplicial.setObjectName("menuComplejo_Simplicial")
        self.menuFunci_n_Booleana = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.menuFunci_n_Booleana.setFont(font)
        self.menuFunci_n_Booleana.setObjectName("menuFunci_n_Booleana")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.menuAyuda.setFont(font)
        self.menuAyuda.setObjectName("menuAyuda")
        self.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNuevo_sc = QtWidgets.QAction(self)
        self.actionNuevo_sc.setObjectName("actionNuevo_sc")
        self.actionListar_sc = QtWidgets.QAction(self)
        self.actionListar_sc.setObjectName("actionListar_sc")
        self.actionNuevo_bf = QtWidgets.QAction(self)
        self.actionNuevo_bf.setObjectName("actionNuevo_bf")
        self.actionListar_bf = QtWidgets.QAction(self)
        self.actionListar_bf.setObjectName("actionListar_bf")
        self.actionAyuda = QtWidgets.QAction(self)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca = QtWidgets.QAction(self)
        self.actionAcerca.setObjectName("actionAcerca")
        self.actionModificar_BF = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/edit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModificar_BF.setIcon(icon1)
        self.actionModificar_BF.setObjectName("actionModificar_BF")
        self.actionTraducir_BF = QtWidgets.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/translation_bf_to_sc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTraducir_BF.setIcon(icon2)
        self.actionTraducir_BF.setObjectName("actionTraducir_BF")
        self.menuComplejo_Simplicial.addAction(self.actionNuevo_sc)
        self.menuComplejo_Simplicial.addAction(self.actionListar_sc)
        self.menuFunci_n_Booleana.addAction(self.actionNuevo_bf)
        self.menuFunci_n_Booleana.addAction(self.actionListar_bf)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca)
        self.menubar.addAction(self.menuComplejo_Simplicial.menuAction())
        self.menubar.addAction(self.menuFunci_n_Booleana.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionModificar_BF)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTraducir_BF)

        header = self.table_outputs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_outputs.setAlternatingRowColors(True)
        self.table_outputs.verticalHeader().setVisible(False)

        self.actionNuevo_sc.triggered.connect(self.open_nuevo_sc)
        self.actionListar_sc.triggered.connect(self.open_listar_sc)
        self.actionNuevo_bf.triggered.connect(self.open_nuevo_bf)
        self.actionListar_bf.triggered.connect(self.open_listar_bf)
        self.actionModificar_BF.triggered.connect(self.add_layout_mod)
        self.actionTraducir_BF.triggered.connect(self.add_layout_tra)
        self.table_outputs.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TFG", "TFG Pablo Ascorbe"))
        self.label_2.setText(_translate("TFG", "Función Booleana"))
        self.label_5.setText(_translate("TFG", "Monótona:"))
        self.label_n_variables.setText(_translate("TFG", "(N_variables)"))
        self.label_monotona.setText(_translate("TFG", "(Monotona)"))
        self.label.setText(_translate("TFG", "Nombre:"))
        item = self.table_outputs.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Posición"))
        item = self.table_outputs.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Valor"))
        self.label_nombre_bf.setText(_translate("TFG", "(Nombre)"))
        self.label_4.setText(_translate("TFG", "Número de Variables:"))
        self.label_3.setText(_translate("TFG", "Salidas:"))
        self.label_6.setText(_translate("TFG", "Nombre de las variables:"))
        self.label_name_variables.setText(_translate("TFG", "(Na_variables)"))
        self.menuComplejo_Simplicial.setTitle(_translate("TFG", "Complejo Simplicial"))
        self.menuFunci_n_Booleana.setTitle(_translate("TFG", "Función Booleana"))
        self.menuAyuda.setTitle(_translate("TFG", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("TFG", "toolBar"))
        self.actionNuevo_sc.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_sc.setShortcut(_translate("TFG", "Ctrl+A"))
        self.actionListar_sc.setText(_translate("TFG", "Cargar"))
        self.actionListar_sc.setShortcut(_translate("TFG", "Ctrl+Q"))
        self.actionNuevo_bf.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_bf.setShortcut(_translate("TFG", "Ctrl+S"))
        self.actionListar_bf.setText(_translate("TFG", "Cargar"))
        self.actionListar_bf.setShortcut(_translate("TFG", "Ctrl+W"))
        self.actionAyuda.setText(_translate("TFG", "Ayuda de TFG Pablo Ascorbe"))
        self.actionAcerca.setText(_translate("TFG", "Acerca de la aplicación"))
        self.actionModificar_BF.setText(_translate("TFG", "Modificar_BF"))
        self.actionModificar_BF.setToolTip(_translate("TFG", "Modificar la Función Booleana"))
        self.actionModificar_BF.setShortcut(_translate("TFG", "Ctrl+1"))
        self.actionTraducir_BF.setText(_translate("TFG", "Traducir_BF"))
        self.actionTraducir_BF.setToolTip(_translate("TFG", "Traducir la función booleana a un complejo simplicial"))

    def set_bf(self, bf):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.bf = bf
        self.label_nombre_bf.setText(bf.name)
        self.label_n_variables.setText(str(bf.num_variables))
        name_var = "("
        for i, elem in enumerate(bf.name_variables):
            name_var += elem
            if i < len(bf.name_variables) - 1:
                name_var += ','
        name_var += ')'
        self.label_name_variables.setText(name_var)
        if bf.monotone_flag:
            self.label_monotona.setText("Sí")
        else:
            self.label_monotona.setText("No")
        self.add_ouputs_table(bf.outputs, bf.num_variables)

    def add_ouputs_table(self, outputs, num):
        self.table_outputs.setRowCount(0)
        if outputs:
            for i in range(2**num):
                numRows = self.table_outputs.rowCount()
                self.table_outputs.insertRow(numRows)
                self.table_outputs.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.table_outputs.setItem(i, 1, QtWidgets.QTableWidgetItem(str(outputs[i])))

    def add_layout_mod(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_dinamico.setContentsMargins(-1, -1, -1, 8)
        self.gridLayout_dinamico.setHorizontalSpacing(7)
        self.gridLayout_dinamico.setVerticalSpacing(20)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 2, 0, 1, 2)
        self.pushButton_Aceptar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton_Aceptar.sizePolicy().hasHeightForWidth())
        self.pushButton_Aceptar.setSizePolicy(sizePolicy)
        self.pushButton_Aceptar.setMinimumSize(QtCore.QSize(150, 25))
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Aceptar, 5, 2, 1, 1, QtCore.Qt.AlignRight)
        self.spin_n_variables = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spin_n_variables.setFont(font)
        self.spin_n_variables.setStyleSheet("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(177, 177, 177);")
        self.spin_n_variables.setObjectName("spin_n_variables")
        self.gridLayout_dinamico.addWidget(self.spin_n_variables, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 3, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 1, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.text_fb_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_fb_name.setFont(font)
        self.text_fb_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_fb_name.setObjectName("text_fb_name")
        self.gridLayout_dinamico.addWidget(self.text_fb_name, 2, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table_ouputs = QtWidgets.QTableWidget(self.centralwidget)
        self.table_ouputs.setMinimumSize(QtCore.QSize(250, 0))
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
        self.horizontalLayout_5.addWidget(self.table_ouputs)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolButton_1 = QtWidgets.QToolButton(self.centralwidget)
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
        self.verticalLayout_3.addWidget(self.toolButton_1)
        self.toolButton_0 = QtWidgets.QToolButton(self.centralwidget)
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
        self.verticalLayout_3.addWidget(self.toolButton_0)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(15, -1, 15, 12)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_name_var = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_name_var.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_name_var.setFont(font)
        self.line_name_var.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(177, 177, 177);")
        self.line_name_var.setObjectName("line_name_var")
        self.horizontalLayout_7.addWidget(self.line_name_var)
        self.toolButton_mas = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_mas.setStyleSheet("QToolButton{\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(71, 71, 71);;}\n"
                                            "\n"
                                            "QToolButton:hover{\n"
                                            "    background-color: rgb(100, 100, 100);\n"
                                            "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/mas.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_mas.setIcon(icon1)
        self.toolButton_mas.setObjectName("toolButton_mas")
        self.horizontalLayout_7.addWidget(self.toolButton_mas)
        self.toolButton_menos = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_menos.setStyleSheet("QToolButton{\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(71, 71, 71);\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton:hover{\n"
                                              "    background-color: rgb(100, 100, 100);\n"
                                              "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/menos.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_menos.setIcon(icon2)
        self.toolButton_menos.setObjectName("toolButton_menos")
        self.horizontalLayout_7.addWidget(self.toolButton_menos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.list_variables = QtWidgets.QListWidget(self.groupBox_2)
        self.list_variables.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_variables.setFont(font)
        self.list_variables.setStyleSheet("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(177, 177, 177);")
        self.list_variables.setObjectName("list_variables")
        self.verticalLayout_4.addWidget(self.list_variables)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.gridLayout_dinamico.addLayout(self.horizontalLayout_5, 4, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("TFG", "Modificar"))
        self.label_7.setText(_translate("TFG", "Nombre de la Función Booleana:"))
        self.pushButton_Aceptar.setText(_translate("TFG", "Aceptar"))
        self.label_8.setText(_translate("TFG", "Número de variables:"))
        item = self.table_ouputs.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Posición"))
        item = self.table_ouputs.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Valor de la salida"))
        self.toolButton_1.setText(_translate("TFG", "1"))
        self.toolButton_0.setText(_translate("TFG", "0"))
        self.groupBox_2.setTitle(_translate("TFG", "Variables"))
        self.line_name_var.setPlaceholderText(_translate("TFG", "Nombre varible"))
        self.toolButton_mas.setText(_translate("TFG", "..."))
        self.toolButton_menos.setText(_translate("TFG", "..."))
        self.label_10.setText(_translate("TFG", "Variables:"))
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.table_ouputs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_ouputs.setAlternatingRowColors(True)
        self.table_ouputs.verticalHeader().setVisible(False)

        self.spin_n_variables.textChanged.connect(self.rellenar_tabla)
        self.pushButton_Aceptar.clicked.connect(self.update_bf)
        self.toolButton_0.clicked.connect(self.put_0_on_focus)
        self.toolButton_1.clicked.connect(self.put_1_on_focus)
        self.toolButton_mas.clicked.connect(self.add_var_to_list)
        self.toolButton_menos.clicked.connect(self.remove_var_from_list)
        self.line_name_var.installEventFilter(self)

        delegate_one_column = DelegateTableOutputs(self.table_ouputs)
        self.table_ouputs.setItemDelegate(delegate_one_column)
        self.rellenar_datos_mod()

    def add_layout_tra(self):
        if self.bf.monotone_flag:
            self.clear_layout_dinamico(self.gridLayout_dinamico)
            self.gridLayout_dinamico = QtWidgets.QGridLayout()
            self.gridLayout_dinamico.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            self.gridLayout_dinamico.setContentsMargins(-1, -1, -1, 8)
            self.gridLayout_dinamico.setHorizontalSpacing(7)
            self.gridLayout_dinamico.setVerticalSpacing(20)
            self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setMaximumSize(QtCore.QSize(350, 50))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label_8")
            self.gridLayout_dinamico.addWidget(self.label_8, 3, 0, 1, 2)
            self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
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
            self.pushButton_Guardar.setObjectName("pushButton_Guardar")
            self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 7, 2, 1, 1, QtCore.Qt.AlignRight)
            self.text_fb_name = QtWidgets.QLineEdit(self.centralwidget)
            self.text_fb_name.setMaximumSize(QtCore.QSize(16777215, 25))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.text_fb_name.setFont(font)
            self.text_fb_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(177, 177, 177);")
            self.text_fb_name.setObjectName("text_fb_name")
            self.gridLayout_dinamico.addWidget(self.text_fb_name, 2, 2, 1, 1)
            self.table_simplex = QtWidgets.QTableWidget(self.centralwidget)
            self.table_simplex.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.table_simplex.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "background-color: rgb(177, 177, 177);")
            self.table_simplex.setAlternatingRowColors(True)
            self.table_simplex.setObjectName("table_simplex")
            self.table_simplex.setColumnCount(3)
            self.table_simplex.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.table_simplex.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.table_simplex.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.table_simplex.setHorizontalHeaderItem(2, item)
            self.gridLayout_dinamico.addWidget(self.table_simplex, 5, 0, 2, 3)
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setMaximumSize(QtCore.QSize(350, 50))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label_7")
            self.gridLayout_dinamico.addWidget(self.label_7, 2, 0, 1, 2)
            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label_9")
            self.gridLayout_dinamico.addWidget(self.label_9, 3, 2, 1, 1)
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")
            self.gridLayout_dinamico.addWidget(self.label_6, 1, 0, 1, 4, QtCore.Qt.AlignHCenter)
            self.label_10 = QtWidgets.QLabel(self.centralwidget)
            self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_10.setFont(font)
            self.label_10.setObjectName("label_10")
            self.gridLayout_dinamico.addWidget(self.label_10, 4, 0, 1, 3)
            self.horizontalLayout.addLayout(self.gridLayout_dinamico)
            _translate = QtCore.QCoreApplication.translate
            self.label_8.setText(_translate("TFG", "Omega:"))
            self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))
            item = self.table_simplex.horizontalHeaderItem(0)
            item.setText(_translate("TFG", "Nombre"))
            item = self.table_simplex.horizontalHeaderItem(1)
            item.setText(_translate("TFG", "Dimension"))
            item = self.table_simplex.horizontalHeaderItem(2)
            item.setText(_translate("TFG", "Caras"))
            self.label_7.setText(_translate("TFG", "Nombre:"))
            self.label_9.setText(_translate("TFG", "(Omega)"))
            self.label_6.setText(_translate("TFG", "Complejo Simplicial Traducido"))
            self.label_10.setText(_translate("TFG", "Simplices:"))
            self.horizontalLayout.setStretch(0, 1)
            self.horizontalLayout.setStretch(1, 1)

            header = self.table_simplex.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

            self.sc_tra = boolean_function_to_simplicial_complex(self.bf)
            self.rellenar_datos_tra(self.sc_tra)

            self.pushButton_Guardar.clicked.connect(self.guardar_sc_traducido)

        else:
            crear_mensaje_error('La función no es monótona y por ello no puede ser traducida en un complejo simplicial',
                                "No Monótona")

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.line_name_var:
            if event.key() == QtCore.Qt.Key_Return and self.line_name_var.hasFocus():
                self.add_var_to_list()
        return super().eventFilter(obj, event)

    def add_var_to_list(self):
        num_var = self.spin_n_variables.text()
        if int(num_var) > self.list_variables.count():
            var = self.line_name_var.text()
            self.line_name_var.clear()
            if self.list_variables.count() == 0:
                self.list_variables.addItem(var)
            else:
                for elem in range(self.list_variables.count()):
                    if var != self.list_variables.item(elem).text():
                        self.list_variables.addItem(var)
        else:
            QMessageBox.information(self, "Error",
                                    "Se ha alcanzado el máximo de variables")

    def remove_var_from_list(self):
        row = self.list_variables.currentRow()
        self.list_variables.takeItem(row)

    def rellenar_tabla(self):
        self.list_variables.clear()
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

    def update_bf(self):
        nombre_bf = self.text_fb_name.text()
        if not nombre_bf:
            crear_mensaje_error('Introduzca el nombre de la función booleana', "Función Booleana")
        elif nombre_invalido(nombre_bf):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.text_fb_name.clear()
        else:
            all_bf = list_boolean_functions()
            edit = False
            if any(x for x in all_bf if x.name != self.label_nombre_bf.text() and x.name == nombre_bf):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Question)
                box.setWindowTitle('GUARDAR')
                box.setText('Ya existe otra Función Booleana con ese nombre \r\n ¿Deseas sobreescribirla?')
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
            names_var = [self.list_variables.item(i).text() for i in range(self.list_variables.count())]
            bf = BooleanFunction(nombre_bf, int(self.spin_n_variables.text()), names_var, outputs)
            bf.set_monotone_flag(Aux.is_monotone(bf.outputs))
            if edit:
                edit_boolean_function(bf)
                remove_boolean_function(self.label_nombre_bf.text())
            elif bf.name != self.label_nombre_bf.text():
                remove_boolean_function(self.label_nombre_bf.text())
                add_boolean_function(bf)
            else:
                update_boolean_function(bf)
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.set_bf(bf)

    def clear_layout_dinamico(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                else:
                    self.clear_layout_dinamico(child.layout())
        self.horizontalLayout.takeAt(1)

    def rellenar_datos_mod(self):
        self.text_fb_name.setText(self.label_nombre_bf.text())
        num = int(self.label_n_variables.text())
        self.spin_n_variables.setValue(int(self.label_n_variables.text()))
        self.table_ouputs.setRowCount(0)
        self.list_variables.addItems(self.bf.name_variables)
        if self.bf.outputs:
            for i in range(2 ** num):
                numRows = self.table_ouputs.rowCount()
                self.table_ouputs.insertRow(numRows)
                self.table_ouputs.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.table_ouputs.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.bf.outputs[i])))

    def rellenar_datos_tra(self, sc_tra):
        self.text_fb_name.setText(sc_tra.name)
        self.label_9.setText(str(sc_tra.omega))
        for i, sim in enumerate(sc_tra.simplex):
            numRows = self.table_simplex.rowCount()
            self.table_simplex.insertRow(numRows)
            self.table_simplex.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
            self.table_simplex.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
            if sim.faces:
                faces_str = "["
                for j, elem in enumerate(sim.faces):
                    faces_str = faces_str + elem.name
                    if j != len(sim.faces) - 1:
                        faces_str = faces_str + ","
                faces_str = faces_str + "]"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(faces_str)
                text_scrolleable.setReadOnly(True)
                if i % 2 != 0:
                    text_scrolleable.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.table_simplex.setCellWidget(i, 2, text_scrolleable)
        self.table_simplex.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def guardar_sc_traducido(self):
        nombre = self.text_fb_name.text()
        if not nombre:
            crear_mensaje_error('Introduzca el nombre del complejo simplicial', "Complejo Simplicial")
        elif nombre_invalido(nombre):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.text_fb_name.clear()
        else:
            self.sc_tra.name = nombre
            edit = False
            all_sc = list_simplicial_complexes()
            if any(x for x in all_sc if x.name == nombre):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Question)
                box.setWindowTitle('GUARDAR')
                box.setText('Ya existe un Complejo simplicial con ese nombre \r\n ¿Deseas sobreescribirlo?')
                box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                buttonY = box.button(QtWidgets.QMessageBox.Yes)
                buttonY.setText('Sí')
                buttonN = box.button(QtWidgets.QMessageBox.No)
                buttonN.setText('No')
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
                box.setWindowIcon(icon)
                box.setStyleSheet("background-image: url(:/images/fondo.png);\n"
                                  "background-color: rgb(27, 27, 27);\n"
                                  "color: rgb(255, 255, 255);")
                buttonN.setStyleSheet("background-color: rgb(71, 71, 71)")
                buttonY.setStyleSheet("background-color: rgb(71, 71, 71)")
                box.exec_()

                if box.clickedButton() == buttonY:
                    edit = True
                else:
                    return
            if edit:
                edit_simplicial_complex(self.sc_tra)
            else:
                add_simplicial_complex(self.sc_tra)
            QMessageBox.information(self, "Éxito",
                                    "Se ha guardado con éxito")

    def set_MenuSC(self, menu_sc):
        self.menu_sc = menu_sc

    def open_nuevo_sc(self):
        self.window_nuevo_sc = NuevoSC(self)
        self.window_nuevo_sc.show()
        self.hide()

    def open_listar_sc(self):
        self.window_listar_sc = ListarSC(self, self.menu_sc, self)
        self.window_listar_sc.show()
        self.hide()

    def open_nuevo_bf(self):
        self.window_nuevo_bf = NuevoBF(self)
        self.window_nuevo_bf.show()
        self.hide()

    def open_listar_bf(self):
        self.window_listar_bf = ListarBF(self, self, self.menu_sc)
        self.window_listar_bf.show()
        self.hide()
