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


class MenuSC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bf = None
        self.setObjectName("TFG")
        self.resize(750, 450)
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
        self.label_nombre_sc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nombre_sc.setFont(font)
        self.label_nombre_sc.setObjectName("label_nombre_sc")
        self.gridLayout_fijo.addWidget(self.label_nombre_sc, 0, 1, 1, 1)
        self.label_omega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_omega.setFont(font)
        self.label_omega.setObjectName("label_omega")
        self.gridLayout_fijo.addWidget(self.label_omega, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_fijo.addWidget(self.label_3, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_fijo.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_fijo.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_dimension = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dimension.setFont(font)
        self.label_dimension.setObjectName("label_dimension")
        self.gridLayout_fijo.addWidget(self.label_dimension, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_fijo.addWidget(self.label_5, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(177, 177, 177);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_fijo.addWidget(self.tableWidget, 4, 0, 1, 2)
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
        self.actionCargar_sc = QtWidgets.QAction(self)
        self.actionCargar_sc.setObjectName("actionCargar_sc")
        self.actionGuardar_sc = QtWidgets.QAction(self)
        self.actionGuardar_sc.setObjectName("actionGuardar_sc")
        self.actionListar_sc = QtWidgets.QAction(self)
        self.actionListar_sc.setObjectName("actionListar_sc")
        self.actionNuevo_bf = QtWidgets.QAction(self)
        self.actionNuevo_bf.setObjectName("actionNuevo_bf")
        self.actionCargar_bf = QtWidgets.QAction(self)
        self.actionCargar_bf.setObjectName("actionCargar_bf")
        self.actionGuardar_bf = QtWidgets.QAction(self)
        self.actionGuardar_bf.setObjectName("actionGuardar_bf")
        self.actionListar_bf = QtWidgets.QAction(self)
        self.actionListar_bf.setObjectName("actionListar_bf")
        self.actionAyuda = QtWidgets.QAction(self)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcerca = QtWidgets.QAction(self)
        self.actionAcerca.setObjectName("actionAcerca")
        self.actionModificar_SC = QtWidgets.QAction(self)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/edit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModificar_SC.setIcon(icon1)
        self.actionModificar_SC.setObjectName("actionModificar_SC")
        self.actionTraducir_SC = QtWidgets.QAction(self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/translation_sc_to_bf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTraducir_SC.setIcon(icon2)
        self.actionTraducir_SC.setObjectName("actionTraducir_SC")
        self.actionLink = QtWidgets.QAction(self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/link.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLink.setIcon(icon3)
        self.actionLink.setObjectName("actionLink")
        self.actionStar = QtWidgets.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/star.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStar.setIcon(icon4)
        self.actionStar.setObjectName("actionStar")
        self.actionJoin = QtWidgets.QAction(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/join.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJoin.setIcon(icon5)
        self.actionJoin.setObjectName("actionJoin")
        self.actionCono = QtWidgets.QAction(self)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/cone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCono.setIcon(icon6)
        self.actionCono.setObjectName("actionCono")
        self.actionCollapsar = QtWidgets.QAction(self)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/collapse.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCollapsar.setIcon(icon7)
        self.actionCollapsar.setObjectName("actionCollapsar")
        self.actionExpandir = QtWidgets.QAction(self)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/expand.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExpandir.setIcon(icon8)
        self.actionExpandir.setObjectName("actionExpandir")
        self.actionCampo_de_Vectores_Manual = QtWidgets.QAction(self)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/manual_vf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCampo_de_Vectores_Manual.setIcon(icon9)
        self.actionCampo_de_Vectores_Manual.setObjectName("actionCampo_de_Vectores_Manual")
        self.actionCampo_de_Vectors_autom_tico = QtWidgets.QAction(self)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/auto_vf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCampo_de_Vectors_autom_tico.setIcon(icon10)
        self.actionCampo_de_Vectors_autom_tico.setObjectName("actionCampo_de_Vectors_autom_tico")
        self.menuComplejo_Simplicial.addAction(self.actionNuevo_sc)
        self.menuComplejo_Simplicial.addAction(self.actionCargar_sc)
        self.menuComplejo_Simplicial.addAction(self.actionGuardar_sc)
        self.menuComplejo_Simplicial.addAction(self.actionListar_sc)
        self.menuFunci_n_Booleana.addAction(self.actionNuevo_bf)
        self.menuFunci_n_Booleana.addAction(self.actionCargar_bf)
        self.menuFunci_n_Booleana.addAction(self.actionGuardar_bf)
        self.menuFunci_n_Booleana.addAction(self.actionListar_bf)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca)
        self.menubar.addAction(self.menuComplejo_Simplicial.menuAction())
        self.menubar.addAction(self.menuFunci_n_Booleana.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionModificar_SC)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTraducir_SC)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLink)
        self.toolBar.addAction(self.actionStar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionJoin)
        self.toolBar.addAction(self.actionCono)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCollapsar)
        self.toolBar.addAction(self.actionExpandir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCampo_de_Vectores_Manual)
        self.toolBar.addAction(self.actionCampo_de_Vectors_autom_tico)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TFG", "TFG Pablo Ascorbe"))
        self.label_2.setText(_translate("TFG", "Complejo Simplicial"))
        self.label_nombre_sc.setText(_translate("TFG", "(Nombre)"))
        self.label_omega.setText(_translate("TFG", "(N_variables)"))
        self.label_3.setText(_translate("TFG", "Salidas:"))
        self.label.setText(_translate("TFG", "Nombre:"))
        self.label_4.setText(_translate("TFG", "Omega:"))
        self.label_dimension.setText(_translate("TFG", "(Monotona)"))
        self.label_5.setText(_translate("TFG", "Dimensión:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Dimensión"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TFG", "Caras"))
        self.menuComplejo_Simplicial.setTitle(_translate("TFG", "Complejo Simplicial"))
        self.menuFunci_n_Booleana.setTitle(_translate("TFG", "Función Booleana"))
        self.menuAyuda.setTitle(_translate("TFG", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("TFG", "toolBar"))
        self.actionNuevo_sc.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_sc.setShortcut(_translate("TFG", "Ctrl+N"))
        self.actionCargar_sc.setText(_translate("TFG", "Cargar"))
        self.actionGuardar_sc.setText(_translate("TFG", "Guardar"))
        self.actionListar_sc.setText(_translate("TFG", "Listar"))
        self.actionNuevo_bf.setText(_translate("TFG", "Nuevo"))
        self.actionCargar_bf.setText(_translate("TFG", "Cargar"))
        self.actionGuardar_bf.setText(_translate("TFG", "Guardar"))
        self.actionListar_bf.setText(_translate("TFG", "Listar"))
        self.actionAyuda.setText(_translate("TFG", "Ayuda de TFG Pablo Ascorbe"))
        self.actionAcerca.setText(_translate("TFG", "Acerca de la aplicación"))
        self.actionModificar_SC.setText(_translate("TFG", "Modificar_SC"))
        self.actionModificar_SC.setToolTip(_translate("TFG", "Modificar el Complejo Simplicial"))
        self.actionModificar_SC.setShortcut(_translate("TFG", "Ctrl+1"))
        self.actionTraducir_SC.setText(_translate("TFG", "Traducir_SC"))
        self.actionTraducir_SC.setToolTip(_translate("TFG", "Traducir el complejo simplicial a una función booleana"))
        self.actionLink.setText(_translate("TFG", "Link"))
        self.actionLink.setToolTip(_translate("TFG", "Calcular Link para un símplice"))
        self.actionStar.setText(_translate("TFG", "Star"))
        self.actionStar.setToolTip(_translate("TFG", "Calcular Star para un símplice"))
        self.actionJoin.setText(_translate("TFG", "Join"))
        self.actionJoin.setToolTip(_translate("TFG", "Calcular el Join del complejo simplicial con otro a seleccionar"))
        self.actionCono.setText(_translate("TFG", "Cono"))
        self.actionCono.setToolTip(_translate("TFG", "Calcular el cono del Complejo Simplicial"))
        self.actionCollapsar.setText(_translate("TFG", "Collapsar"))
        self.actionCollapsar.setToolTip(_translate("TFG", "Collapsar el Complejo Simplicial"))
        self.actionExpandir.setText(_translate("TFG", "Expandir"))
        self.actionExpandir.setToolTip(_translate("TFG", "Expandir el Complejo Simplicial"))
        self.actionCampo_de_Vectores_Manual.setText(_translate("TFG", "Campo de Vectores Manual"))
        self.actionCampo_de_Vectores_Manual.setToolTip(_translate("TFG", "Calcular un campo de vectores manualmente"))
        self.actionCampo_de_Vectors_autom_tico.setText(_translate("TFG", "Campo de Vectors automático"))
        self.actionCampo_de_Vectors_autom_tico.setToolTip(
            _translate("TFG", "Calcular un campo de vectores automáticamente"))

    def set_sc(self, sc):
        # self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.sc = sc
        self.label_nombre_sc.setText(sc.name)
        self.label_dimension.setText(str(sc.dimension))
        self.label_omega.setText(str(sc.omega))
        # self.add_ouputs_table(bf.outputs, bf.num_variables)
