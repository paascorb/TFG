from PyQt5.QtWidgets import QWidget, QItemDelegate, QMainWindow, QTextEdit

from PyQt5 import QtCore, QtGui, QtWidgets

from LogicaDeNegocio import Join
from LogicaDeNegocio.BooleanFunctionManager import *
from LogicaDeNegocio.Join import *
from LogicaDeNegocio.SimplicialComplexManager import *
import ModeloDeDominio.Auxiliary as Aux
from LogicaDeNegocio.Traductor import simplicial_complex_to_boolean_function
from LogicaDeNegocio.VectorFieldResolver import resolve_field
from Presentacion.Listar_BF import ListarBF
from Presentacion.Listar_SC import ListarSC
from Presentacion.Nuevo_BF import NuevoBF
from Presentacion.Nuevo_SC import NuevoSC
from Presentacion.Nuevo_VF import NuevoVF
from Presentacion.PresentacionAuxiliar import *


class MenuSC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.expand = None
        self.colapso = None
        self.join = None
        self.link = None
        self.star = None
        self.sc = None
        self.sc_cone = None
        self.vf_auto = None
        self.bf_tra = None
        self.bf = None
        self.faces = list()
        self.simplex = list()
        self.setObjectName("TFG")
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
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
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
        self.gridLayout_dinamico.setHorizontalSpacing(10)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/flechas.png"))
        self.menubar.children()[0].setIconSize(QtCore.QSize(100, 100))
        self.menubar.children()[0].setIcon(icon)
        self.menubar.adjustSize()
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/flechas.png"))
        self.toolBar.children()[1].setIconSize(QtCore.QSize(100, 100))
        self.toolBar.children()[1].setIcon(icon)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNuevo_sc = QtWidgets.QAction(self)
        self.actionNuevo_sc.setObjectName("actionNuevo_sc")
        self.actionListar_sc = QtWidgets.QAction(self)
        self.actionListar_sc.setObjectName("actionCargar_sc")
        self.actionNuevo_bf = QtWidgets.QAction(self)
        self.actionNuevo_bf.setObjectName("actionNuevo_bf")
        self.actionListar_bf = QtWidgets.QAction(self)
        self.actionListar_bf.setObjectName("actionCargar_bf")
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
        self.actionCampo_De_Vectores = QtWidgets.QAction(self)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/vector_field.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCampo_De_Vectores.setIcon(icon11)
        self.actionCampo_De_Vectores.setObjectName("actionCampo_De_Vectores")
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
        self.toolBar.addAction(self.actionCampo_De_Vectores)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setAlternatingRowColors(True)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionNuevo_sc.triggered.connect(self.open_nuevo_sc)
        self.actionListar_sc.triggered.connect(self.open_listar_sc)
        self.actionNuevo_bf.triggered.connect(self.open_nuevo_bf)
        self.actionListar_bf.triggered.connect(self.open_listar_bf)

        self.actionModificar_SC.triggered.connect(self.add_layout_mod)
        self.actionTraducir_SC.triggered.connect(self.add_layout_tra)
        self.actionCampo_de_Vectores_Manual.triggered.connect(self.open_nuevo_vf)
        self.actionCampo_De_Vectores.triggered.connect(self.add_layout_vf)
        self.actionCampo_de_Vectors_autom_tico.triggered.connect(self.add_layout_vf_auto)
        self.actionCono.triggered.connect(self.add_layout_cone)
        self.actionLink.triggered.connect(self.add_layout_link)
        self.actionStar.triggered.connect(self.add_layout_star)
        self.actionJoin.triggered.connect(self.add_layout_join)
        self.actionCollapsar.triggered.connect(self.add_layout_collapse)
        self.actionExpandir.triggered.connect(self.add_layout_expansion)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TFG", "TFG Pablo Ascorbe"))
        self.label_2.setText(_translate("TFG", "Complejo Simplicial"))
        self.label_nombre_sc.setText(_translate("TFG", "(Nombre)"))
        self.label_omega.setText(_translate("TFG", "(N_variables)"))
        self.label_3.setText(_translate("TFG", "Símplices:"))
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
        self.actionNuevo_sc.setShortcut(_translate("TFG", "Ctrl+A"))
        self.actionListar_sc.setText(_translate("TFG", "Cargar"))
        self.actionListar_sc.setShortcut(_translate("TFG", "Ctrl+Q"))
        self.actionNuevo_bf.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_bf.setShortcut(_translate("TFG", "Ctrl+S"))
        self.actionListar_bf.setText(_translate("TFG", "Cargar"))
        self.actionListar_bf.setShortcut(_translate("TFG", "Ctrl+W"))
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
        self.actionCampo_De_Vectores.setText(_translate("TFG", "Campo De Vectores"))
        self.actionCampo_De_Vectores.setToolTip(_translate("TFG",
                                                           "Ver todos los campos de vectores asociados al complejo "
                                                           "simplicial"))
        self.actionCampo_de_Vectors_autom_tico.setToolTip(
            _translate("TFG", "Calcular un campo de vectores automáticamente"))

    def set_sc(self, sc):
        self.sc = sc
        self.label_nombre_sc.setText(sc.name)
        self.label_dimension.setText(str(sc.dimension))
        self.label_omega.setText(str(sc.omega))
        self.add_simplex_table(sc.simplex)
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 0)

    def add_layout_tra(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(0, 4, 15, 10)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(11)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 6, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 2, 1, 1, 1)
        self.table_outputs = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_outputs.sizePolicy().hasHeightForWidth())
        self.table_outputs.setSizePolicy(sizePolicy)
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
        self.gridLayout_dinamico.addWidget(self.table_outputs, 5, 1, 1, 2)
        self.label_monotona = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_monotona.setFont(font)
        self.label_monotona.setObjectName("label_monotona")
        self.gridLayout_dinamico.addWidget(self.label_monotona, 4, 2, 1, 1)
        self.label_n_variables = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_n_variables.setFont(font)
        self.label_n_variables.setObjectName("label_n_variables")
        self.gridLayout_dinamico.addWidget(self.label_n_variables, 2, 2, 1, 1)
        self.text_fb_name = QtWidgets.QLineEdit(self.centralwidget)
        self.text_fb_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_fb_name.setFont(font)
        self.text_fb_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_fb_name.setObjectName("text_fb_name")
        self.gridLayout_dinamico.addWidget(self.text_fb_name, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_dinamico.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_name_variables = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name_variables.setFont(font)
        self.label_name_variables.setObjectName("label_name_variables")
        self.gridLayout_dinamico.addWidget(self.label_name_variables, 3, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        _translate = QtCore.QCoreApplication.translate

        self.label_n_variables.setText(_translate("TFG", "(N_variables)"))
        self.label_8.setText(_translate("TFG", "Número de Variables:"))
        self.label_7.setText(_translate("TFG", "Nombre:"))
        self.label_6.setText(_translate("TFG", "Función Booleana Traducida"))
        self.label_9.setText(_translate("TFG", "Monótona:"))
        self.label_10.setText(_translate("TFG", "Nombre de las variables:"))
        self.label_name_variables.setText(_translate("TFG", "(Na_variables)"))
        self.label_monotona.setText(_translate("TFG", "(Monotona)"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))
        item = self.table_outputs.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Posición"))
        item = self.table_outputs.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Valor"))

        header = self.table_outputs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.table_outputs.setAlternatingRowColors(True)
        self.table_outputs.verticalHeader().setVisible(False)
        delegate_one_column = DelegateTableOutputs(self.table_outputs)
        self.table_outputs.setItemDelegate(delegate_one_column)

        self.bf_tra = simplicial_complex_to_boolean_function(self.sc)
        if Aux.is_monotone(self.bf_tra.outputs):
            self.bf_tra.monotone_flag = True
        self.rellenar_datos_tra(self.bf_tra)

        self.pushButton_Guardar.clicked.connect(self.guardar_bf_traducido)

    def rellenar_datos_tra(self, bf):
        self.text_fb_name.setText(bf.name)
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
        self.add_ouputs_table_tra(bf.outputs, bf.num_variables)

    def add_ouputs_table_tra(self, outputs, num):
        self.table_outputs.setRowCount(0)
        if outputs:
            for i in range(2 ** num):
                numRows = self.table_outputs.rowCount()
                self.table_outputs.insertRow(numRows)
                self.table_outputs.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.table_outputs.setItem(i, 1, QtWidgets.QTableWidgetItem(str(outputs[i])))

    def guardar_bf_traducido(self):
        nombre = self.text_fb_name.text()
        if not nombre:
            crear_mensaje_error('Introduzca el nombre de la función booleana', "Función booleana")
        elif nombre_invalido(nombre):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.text_fb_name.clear()
        else:
            self.bf_tra.name = nombre
            edit = False
            all_bf = list_boolean_functions()
            if any(x for x in all_bf if x.name == nombre):
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
                edit_boolean_function(self.bf_tra)
            else:
                add_boolean_function(self.bf_tra)
            QMessageBox.information(self, "Éxito",
                                    "Se ha guardado con éxito")

    def add_layout_mod(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 0, 1, 1)
        self.text_sc_name = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_sc_name.sizePolicy().hasHeightForWidth())
        self.text_sc_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_sc_name.setFont(font)
        self.text_sc_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_sc_name.setObjectName("text_sc_name")
        self.gridLayout_dinamico.addWidget(self.text_sc_name, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.list_simplex = QtWidgets.QListWidget(self.groupBox)
        self.list_simplex.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.list_simplex.setFont(font)
        self.list_simplex.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.list_simplex.setAlternatingRowColors(True)
        self.list_simplex.setObjectName("list_simplex")
        self.gridLayout_3.addWidget(self.list_simplex, 0, 0, 1, 2)
        self.pushButton_QuitarSim = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_QuitarSim.sizePolicy().hasHeightForWidth())
        self.pushButton_QuitarSim.setSizePolicy(sizePolicy)
        self.pushButton_QuitarSim.setMinimumSize(QtCore.QSize(200, 25))
        self.pushButton_QuitarSim.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_QuitarSim.setFont(font)
        self.pushButton_QuitarSim.setStyleSheet("QPushButton{\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(71, 71, 71);\n"
                                                "border: 1px solid;\n"
                                                "border-radius: 10px;}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: rgb(100, 100, 100);\n"
                                                "}")
        self.pushButton_QuitarSim.setObjectName("pushButton_QuitarSim")
        self.gridLayout_3.addWidget(self.pushButton_QuitarSim, 1, 0, 1, 2)
        self.gridLayout_dinamico.addWidget(self.groupBox, 0, 1, 3, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text_dim_sim = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_dim_sim.setFont(font)
        self.text_dim_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_dim_sim.setObjectName("text_dim_sim")
        self.gridLayout_4.addWidget(self.text_dim_sim, 3, 1, 1, 1)
        self.posible_faces = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.posible_faces.setFont(font)
        self.posible_faces.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.posible_faces.setObjectName("posible_faces")
        self.gridLayout_4.addWidget(self.posible_faces, 4, 1, 1, 1)
        self.list_faces = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_faces.sizePolicy().hasHeightForWidth())
        self.list_faces.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_faces.setFont(font)
        self.list_faces.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(177, 177, 177);")
        self.list_faces.setAlternatingRowColors(True)
        self.list_faces.setObjectName("list_faces")
        self.gridLayout_4.addWidget(self.list_faces, 7, 0, 1, 2)
        self.text_nombre_sim = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_nombre_sim.setFont(font)
        self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(177, 177, 177);")
        self.text_nombre_sim.setObjectName("text_nombre_sim")
        self.gridLayout_4.addWidget(self.text_nombre_sim, 2, 0, 1, 2)
        self.pushButton_Anadir = QtWidgets.QPushButton(self.groupBox_2)
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
        self.gridLayout_4.addWidget(self.pushButton_Anadir, 8, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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
        self.horizontalLayout_2.addWidget(self.toolButton_mas)
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
        self.horizontalLayout_2.addWidget(self.toolButton_menos)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)
        self.gridLayout_dinamico.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
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
        self.gridLayout_6.addWidget(self.pushButton_Aceptar, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_dinamico.addLayout(self.gridLayout_6, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("TFG", "Nombre del Complejo simplicial:"))
        self.groupBox.setTitle(_translate("TFG", "Símplices"))
        self.pushButton_QuitarSim.setText(_translate("TFG", "Quitar"))
        self.groupBox_2.setTitle(_translate("TFG", "Añadir Símplice"))
        self.pushButton_Anadir.setText(_translate("TFG", "Añadir"))
        self.label_7.setText(_translate("TFG", "Caras"))
        self.toolButton_mas.setText(_translate("TFG", "..."))
        self.toolButton_menos.setText(_translate("TFG", "..."))
        self.label_8.setText(_translate("TFG", "Nombre del Símplice:"))
        self.label_9.setText(_translate("TFG", "Dimensión:"))
        self.pushButton_Aceptar.setText(_translate("TFG", "Aceptar"))

        self.text_sc_name.setText(self.label_nombre_sc.text())

        self.simplex = self.sc.simplex.copy()

        self.populate_simplex_list_mod(self.sc.simplex)
        self.pushButton_Aceptar.clicked.connect(self.update_sc)
        self.pushButton_QuitarSim.clicked.connect(self.remove_simplex)
        self.pushButton_Anadir.clicked.connect(self.add_simplex)
        self.text_nombre_sim.installEventFilter(self)
        self.text_dim_sim.textChanged.connect(self.add_posible_faces)
        self.toolButton_mas.clicked.connect(self.add_face_to_list)
        self.toolButton_menos.clicked.connect(self.remove_face_of_list)

    def add_layout_vf(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        if self.sc.vector_fields:
            self.comboBox_vf = QtWidgets.QComboBox(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.comboBox_vf.setFont(font)
            self.comboBox_vf.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(177, 177, 177);")
            self.comboBox_vf.setObjectName("comboBox_vf")
            self.gridLayout_dinamico.addWidget(self.comboBox_vf, 1, 1, 1, 2)
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label_7")
            self.gridLayout_dinamico.addWidget(self.label_7, 2, 1, 1, 1)
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")
            self.gridLayout_dinamico.addWidget(self.label_6, 0, 1, 1, 2)
            self.table_vf = QtWidgets.QTableWidget(self.centralwidget)
            self.table_vf.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
            self.table_vf.setObjectName("table_vf")
            self.table_vf.setColumnCount(2)
            self.table_vf.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.table_vf.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(12)
            item.setFont(font)
            self.table_vf.setHorizontalHeaderItem(1, item)
            self.gridLayout_dinamico.addWidget(self.table_vf, 4, 1, 1, 2)
            self.label_vf_name = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_vf_name.setFont(font)
            self.label_vf_name.setText("")
            self.label_vf_name.setObjectName("label_vf_name")
            self.gridLayout_dinamico.addWidget(self.label_vf_name, 2, 2, 1, 1)
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label_8")
            self.gridLayout_dinamico.addWidget(self.label_8, 3, 1, 1, 2)
            self.horizontalLayout.addLayout(self.gridLayout_dinamico)
            self.horizontalLayout.setStretch(0, 1)
            self.horizontalLayout.setStretch(1, 1)

            _translate = QtCore.QCoreApplication.translate
            self.comboBox_vf.setPlaceholderText(_translate("TFG", "Seleccione un campo"))
            self.label_7.setText(_translate("TFG", "Nombre:"))
            self.label_6.setText(_translate("TFG", "Campos de vectores"))
            item = self.table_vf.horizontalHeaderItem(0)
            item.setText(_translate("TFG", "Inicio"))
            item = self.table_vf.horizontalHeaderItem(1)
            item.setText(_translate("TFG", "Alcanzables"))
            self.label_8.setText(_translate("TFG", "Rutas:"))

            header = self.table_vf.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            self.table_vf.setAlternatingRowColors(True)
            self.table_vf.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.comboBox_vf.addItems([x.name for x in self.sc.vector_fields])
            self.gridLayout_dinamico.setVerticalSpacing(15)
            self.gridLayout_dinamico.setContentsMargins(0, 4, 15, 20)

            self.comboBox_vf.currentTextChanged.connect(self.rellenar_datos_vf)

        else:
            QMessageBox.information(self, "Imposible",
                                    "El complejo simplicial seleccionado no dispone de ningún campo")

    def add_layout_vf_auto(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(0, 4, 15, 10)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(10)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 2, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 1, 1, 1, 1)
        self.table_vf = QtWidgets.QTableWidget(self.centralwidget)
        self.table_vf.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.table_vf.setObjectName("table_vf")
        self.table_vf.setColumnCount(2)
        self.table_vf.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_vf.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_vf.setHorizontalHeaderItem(1, item)
        self.gridLayout_dinamico.addWidget(self.table_vf, 5, 1, 1, 2)
        self.line_vf_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_vf_name.setFont(font)
        self.line_vf_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.line_vf_name.setObjectName("line_vf_name")
        self.gridLayout_dinamico.addWidget(self.line_vf_name, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 1, 1, 2)
        self.tablePairs = QtWidgets.QTableWidget(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.tablePairs, 3, 1, 1, 2)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 6, 2, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.tablePairs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        header = self.table_vf.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablePairs.setFont(font)
        self.table_vf.setFont(font)

        self.tablePairs.setItemDelegate(AligDelegate())
        self.table_vf.setItemDelegate(AligDelegate())

        self.tablePairs.setAlternatingRowColors(True)
        self.table_vf.setAlternatingRowColors(True)

        self.tablePairs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_vf.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        _translate = QtCore.QCoreApplication.translate

        resolve_field(self.sc.create_vector_field("Default"), self.sc)
        self.vf_auto = self.sc.vector_fields[len(self.sc.vector_fields) - 1]
        self.sc.vector_fields.pop()
        self.rellenar_tablas_vf_auto()

        self.pushButton_Guardar.clicked.connect(self.guardar_vf_auto)

        self.label_9.setText(_translate("TFG", "Parejas Añadidas:"))
        self.label_7.setText(_translate("TFG", "Nombre:"))
        item = self.table_vf.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Inicio"))
        item = self.table_vf.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Alcanzables"))
        self.line_vf_name.setPlaceholderText(_translate("TFG", "Nombre"))
        self.label_8.setText(_translate("TFG", "Rutas:"))
        self.label_6.setText(_translate("TFG", "Campo de vectores autogenerado"))
        item = self.tablePairs.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Sigma"))
        item = self.tablePairs.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Tau"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))

    def add_layout_cone(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        input_dialog = QtWidgets.QInputDialog(self)
        input_dialog.setCancelButtonText("Cancelar")
        input_dialog.setOkButtonText("Aceptar")
        input_dialog.setWindowTitle("Nombre vértice")
        input_dialog.setLabelText("Nombre del vértice del cono:")

        if input_dialog.exec_() == QtWidgets.QDialog.Accepted:
            cone_name = input_dialog.textValue()
            for elem in self.sc.simplex[:self.sc.c_vector[0]]:
                if elem.name == cone_name:
                    crear_mensaje_error('Ya existe un vértice con ese nombre', "Nombre inválido")
                    self.clear_layout_dinamico(self.gridLayout_dinamico)
                    return
        else:
            self.clear_layout_dinamico(self.gridLayout_dinamico)
            return
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(0, 4, 15, 10)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(10)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_cone_omega = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cone_omega.setFont(font)
        self.label_cone_omega.setObjectName("label_cone_omega")
        self.gridLayout_dinamico.addWidget(self.label_cone_omega, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_dinamico.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_dinamico.addWidget(self.label_12, 4, 1, 1, 2)
        self.line_cone_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_cone_name.setFont(font)
        self.line_cone_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(177, 177, 177);")
        self.line_cone_name.setObjectName("line_cone_name")
        self.gridLayout_dinamico.addWidget(self.line_cone_name, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 1, 1, 2)
        self.label_cone_dim = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cone_dim.setFont(font)
        self.label_cone_dim.setObjectName("label_cone_dim")
        self.gridLayout_dinamico.addWidget(self.label_cone_dim, 3, 2, 1, 1)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 6, 2, 1, 1, QtCore.Qt.AlignRight)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.gridLayout_dinamico.addWidget(self.tableWidget_2, 5, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)

        self.tableWidget_2.setItemDelegate(AligDelegate())
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.sc_cone = cono(self.sc, cone_name)

        _translate = QtCore.QCoreApplication.translate

        self.label_cone_omega.setText(_translate("TFG", str(self.sc_cone.omega)))
        self.label_10.setText(_translate("TFG", "Dimensión"))
        self.label_7.setText(_translate("TFG", "Nombre:"))
        self.label_12.setText(_translate("TFG", "Símplices:"))
        self.line_cone_name.setPlaceholderText(_translate("TFG", "Cono"))
        self.label_9.setText(_translate("TFG", "Omega:"))
        self.label_6.setText(_translate("TFG", "Cono de " + self.sc.name))
        self.label_cone_dim.setText(_translate("TFG", str(self.sc_cone.dimension)))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Dimensión"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("TFG", "Caras"))

        self.pushButton_Guardar.clicked.connect(self.save_cone)

        self.rellenar_tabla_cono()

    def add_layout_star(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(5, -1, 5, -1)
        self.gridLayout_dinamico.setSpacing(15)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.list_sim_star = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_sim_star.setFont(font)
        self.list_sim_star.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.list_sim_star.setAlternatingRowColors(True)
        self.list_sim_star.setObjectName("list_sim_star")
        self.gridLayout_dinamico.addWidget(self.list_sim_star, 5, 0, 1, 2)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_dinamico.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 1, 0, 2, 1)
        self.comboBox_sim_star = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_sim_star.setFont(font)
        self.comboBox_sim_star.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "background-color: rgb(177, 177, 177);")
        self.comboBox_sim_star.setObjectName("comboBox_sim_star")
        self.gridLayout_dinamico.addWidget(self.comboBox_sim_star, 1, 1, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.rellenar_combo_sim_stlk(self.comboBox_sim_star)
        self.comboBox_sim_star.currentIndexChanged.connect(self.rellenar_tabla_star)
        self.reset_listWidget(self.list_sim_star)
        self.pushButton_Guardar.clicked.connect(self.save_star)

        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("TFG", "Seleccione el vértice:"))
        self.label_6.setText(_translate("TFG", "Cálculo del Star"))
        self.label_8.setText(_translate("TFG", "Star:"))
        self.lineEdit.setPlaceholderText(_translate("TFG", "Nombre"))
        self.label_9.setText(_translate("TFG", "Nombre:"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))

    def add_layout_link(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(5, -1, 5, -1)
        self.gridLayout_dinamico.setSpacing(15)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.list_sim_link = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_sim_link.setFont(font)
        self.list_sim_link.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.list_sim_link.setAlternatingRowColors(True)
        self.list_sim_link.setObjectName("list_sim_star")
        self.gridLayout_dinamico.addWidget(self.list_sim_link, 5, 0, 1, 2)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(177, 177, 177);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_dinamico.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 1, 0, 2, 1)
        self.comboBox_sim_link = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_sim_link.setFont(font)
        self.comboBox_sim_link.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "background-color: rgb(177, 177, 177);")
        self.comboBox_sim_link.setObjectName("comboBox_sim_star")
        self.gridLayout_dinamico.addWidget(self.comboBox_sim_link, 1, 1, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.rellenar_combo_sim_stlk(self.comboBox_sim_link)
        self.comboBox_sim_link.currentIndexChanged.connect(self.rellenar_tabla_link)
        self.reset_listWidget(self.list_sim_link)
        self.pushButton_Guardar.clicked.connect(self.save_link)

        _translate = QtCore.QCoreApplication.translate
        self.label_7.setText(_translate("TFG", "Seleccione el vértice:"))
        self.label_6.setText(_translate("TFG", "Cálculo del Link"))
        self.label_8.setText(_translate("TFG", "Link:"))
        self.lineEdit.setPlaceholderText(_translate("TFG", "Nombre"))
        self.label_9.setText(_translate("TFG", "Nombre:"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))

    def add_layout_join(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(5, -1, 5, 15)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(12)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 5, 0, 1, 2)
        self.label_dimension_join = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dimension_join.setFont(font)
        self.label_dimension_join.setObjectName("label_dimension_join")
        self.gridLayout_dinamico.addWidget(self.label_dimension_join, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 3, 0, 1, 1)
        self.line_join_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_join_name.setFont(font)
        self.line_join_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(177, 177, 177);")
        self.line_join_name.setObjectName("line_join_name")
        self.gridLayout_dinamico.addWidget(self.line_join_name, 2, 1, 1, 1)
        self.combo_join = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_join.setFont(font)
        self.combo_join.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(177, 177, 177);")
        self.combo_join.setObjectName("combo_join")
        self.gridLayout_dinamico.addWidget(self.combo_join, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_omega_join = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_omega_join.setFont(font)
        self.label_omega_join.setObjectName("label_omega_join")
        self.gridLayout_dinamico.addWidget(self.label_omega_join, 3, 1, 1, 1)
        self.label_join = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_join.setFont(font)
        self.label_join.setObjectName("label_join")
        self.gridLayout_dinamico.addWidget(self.label_join, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 2, 0, 1, 1)
        self.table_join = QtWidgets.QTableWidget(self.centralwidget)
        self.table_join.setMinimumSize(QtCore.QSize(300, 0))
        self.table_join.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(177, 177, 177);")
        self.table_join.setObjectName("table_join")
        self.table_join.setColumnCount(3)
        self.table_join.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_join.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_join.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_join.setHorizontalHeaderItem(2, item)
        self.gridLayout_dinamico.addWidget(self.table_join, 6, 0, 1, 2)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 7, 1, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.table_join.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_join.setAlternatingRowColors(True)
        self.table_join.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("TFG", "Dimensión:"))
        self.label_7.setText(_translate("TFG", "Omega:"))
        self.label_join.setText(_translate("TFG", "Join de ..."))
        self.line_join_name.setPlaceholderText(_translate("TFG", "Nombre"))
        self.label_6.setText(_translate("TFG", "Nombre:"))
        self.label_9.setText(_translate("TFG", "Salidas:"))
        self.label_dimension_join.setText(_translate("TFG", "(Dimensión)"))
        self.label_omega_join.setText(_translate("TFG", "(N_variables)"))
        item = self.table_join.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Nombre"))
        item = self.table_join.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Dimensión"))
        item = self.table_join.horizontalHeaderItem(2)
        item.setText(_translate("TFG", "Caras"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))

        self.set_join_ui()
        self.combo_join.currentIndexChanged.connect(self.compute_join)
        self.pushButton_Guardar.clicked.connect(self.save_join)

    def add_layout_collapse(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.colapso = None
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(5, -1, 5, 15)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(12)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_dinamico.addWidget(self.label_7, 3, 0, 1, 1)
        self.combo_sigma = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_sigma.setFont(font)
        self.combo_sigma.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(177, 177, 177);")
        self.combo_sigma.setObjectName("combo_sigma")
        self.gridLayout_dinamico.addWidget(self.combo_sigma, 3, 1, 1, 1)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 7, 1, 1, 1, QtCore.Qt.AlignRight)
        self.combo_tau = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_tau.setFont(font)
        self.combo_tau.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(177, 177, 177);")
        self.combo_tau.setObjectName("combo_tau")
        self.gridLayout_dinamico.addWidget(self.combo_tau, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_dinamico.addWidget(self.label_9, 5, 0, 1, 2)
        self.table_colapso = QtWidgets.QTableWidget(self.centralwidget)
        self.table_colapso.setMinimumSize(QtCore.QSize(300, 0))
        self.table_colapso.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.table_colapso.setObjectName("table_colapso")
        self.table_colapso.setColumnCount(3)
        self.table_colapso.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_colapso.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_colapso.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.table_colapso.setHorizontalHeaderItem(2, item)
        self.gridLayout_dinamico.addWidget(self.table_colapso, 6, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_dinamico.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_dinamico.addWidget(self.label_10, 1, 0, 1, 1)
        self.line_cone_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_cone_name.setFont(font)
        self.line_cone_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(177, 177, 177);")
        self.line_cone_name.setObjectName("line_cone_name")
        self.gridLayout_dinamico.addWidget(self.line_cone_name, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.table_colapso.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.table_colapso.setAlternatingRowColors(True)
        self.table_colapso.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.rellenar_combo_tau_colapso()

        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("TFG", "Colapso elemental"))
        self.label_7.setText(_translate("TFG", "Sigma:"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))
        self.label_9.setText(_translate("TFG", "Resultado"))
        item = self.table_colapso.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Nombre"))
        item = self.table_colapso.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Dimensión"))
        item = self.table_colapso.horizontalHeaderItem(2)
        item.setText(_translate("TFG", "Caras"))
        self.label_8.setText(_translate("TFG", "Tau:"))
        self.label_10.setText(_translate("TFG", "Nombre:"))
        self.line_cone_name.setPlaceholderText(_translate("TFG", "Colapso Elemental"))

        self.pushButton_Guardar.clicked.connect(self.save_colapso)

    def add_layout_expansion(self):
        self.clear_layout_dinamico(self.gridLayout_dinamico)
        self.gridLayout_dinamico = QtWidgets.QGridLayout()
        self.gridLayout_dinamico.setContentsMargins(5, -1, 5, 15)
        self.gridLayout_dinamico.setHorizontalSpacing(15)
        self.gridLayout_dinamico.setVerticalSpacing(12)
        self.gridLayout_dinamico.setObjectName("gridLayout_dinamico")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.gridLayout_dinamico.addWidget(self.tableWidget_2, 4, 0, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_dinamico.addWidget(self.label_10, 3, 0, 1, 2)
        self.line_cone_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_cone_name.setFont(font)
        self.line_cone_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(177, 177, 177);")
        self.line_cone_name.setObjectName("line_cone_name")
        self.gridLayout_dinamico.addWidget(self.line_cone_name, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.posible_faces = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.posible_faces.setFont(font)
        self.posible_faces.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.posible_faces.setObjectName("posible_faces")
        self.gridLayout_3.addWidget(self.posible_faces, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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
        self.horizontalLayout_2.addWidget(self.toolButton_mas)
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
        self.horizontalLayout_2.addWidget(self.toolButton_menos)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)
        self.list_faces = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_faces.sizePolicy().hasHeightForWidth())
        self.list_faces.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_faces.setFont(font)
        self.list_faces.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(177, 177, 177);")
        self.list_faces.setAlternatingRowColors(True)
        self.list_faces.setObjectName("list_faces")
        self.gridLayout_3.addWidget(self.list_faces, 7, 0, 1, 2)
        self.text_nombre_sim = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_nombre_sim.setFont(font)
        self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(177, 177, 177);")
        self.text_nombre_sim.setObjectName("text_nombre_sim")
        self.gridLayout_3.addWidget(self.text_nombre_sim, 2, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.text_dim_sim = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_dim_sim.setFont(font)
        self.text_dim_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_dim_sim.setObjectName("text_dim_sim")
        self.gridLayout_3.addWidget(self.text_dim_sim, 3, 1, 1, 1)
        self.pushButton_Anadir = QtWidgets.QPushButton(self.groupBox_2)
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
        self.gridLayout_3.addWidget(self.pushButton_Anadir, 8, 0, 1, 2)
        self.gridLayout_dinamico.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.list_simplex = QtWidgets.QListWidget(self.groupBox)
        self.list_simplex.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.list_simplex.setFont(font)
        self.list_simplex.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.list_simplex.setAlternatingRowColors(True)
        self.list_simplex.setObjectName("list_simplex")
        self.gridLayout_4.addWidget(self.list_simplex, 0, 0, 1, 2)
        self.pushButton_QuitarSim = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_QuitarSim.sizePolicy().hasHeightForWidth())
        self.pushButton_QuitarSim.setSizePolicy(sizePolicy)
        self.pushButton_QuitarSim.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_QuitarSim.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_QuitarSim.setBaseSize(QtCore.QSize(0, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_QuitarSim.setFont(font)
        self.pushButton_QuitarSim.setStyleSheet("QPushButton{\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(71, 71, 71);\n"
                                                "border: 1px solid;\n"
                                                "border-radius: 10px;}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: rgb(100, 100, 100);\n"
                                                "}")
        self.pushButton_QuitarSim.setObjectName("pushButton_QuitarSim")
        self.gridLayout_4.addWidget(self.pushButton_QuitarSim, 1, 0, 1, 2)
        self.gridLayout_dinamico.addWidget(self.groupBox, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_dinamico.addWidget(self.label_6, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_dinamico.addWidget(self.label_11, 1, 0, 1, 1)
        self.pushButton_Guardar = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_dinamico.addWidget(self.pushButton_Guardar, 5, 1, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addLayout(self.gridLayout_dinamico)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("TFG", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("TFG", "Dimensión"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("TFG", "Caras"))
        self.label_10.setText(_translate("TFG", "Resultado"))
        self.line_cone_name.setPlaceholderText(_translate("TFG", "Expansión Elemental"))
        self.groupBox_2.setTitle(_translate("TFG", "Añadir Pareja"))
        self.label_7.setText(_translate("TFG", "Caras"))
        self.toolButton_mas.setText(_translate("TFG", "..."))
        self.toolButton_menos.setText(_translate("TFG", "..."))
        self.label_8.setText(_translate("TFG", "Nombre del Símplice:"))
        self.label_9.setText(_translate("TFG", "Dimensión:"))
        self.pushButton_Anadir.setText(_translate("TFG", "Añadir"))
        self.groupBox.setTitle(_translate("TFG", "Pareja"))
        __sortingEnabled = self.list_simplex.isSortingEnabled()
        self.list_simplex.setSortingEnabled(False)
        self.list_simplex.setSortingEnabled(__sortingEnabled)
        self.pushButton_QuitarSim.setText(_translate("TFG", "Quitar"))
        self.label_6.setText(_translate("TFG", "Expansión"))
        self.label_11.setText(_translate("TFG", "Nombre"))
        self.pushButton_Guardar.setText(_translate("TFG", "Guardar"))

        self.pushButton_Anadir.clicked.connect(self.add_simplex_exp)
        self.pushButton_QuitarSim.clicked.connect(self.remove_simplex_exp)
        self.toolButton_mas.clicked.connect(self.add_face_to_list_exp)
        self.text_dim_sim.textChanged.connect(self.add_posible_faces_exp)
        self.toolButton_menos.clicked.connect(self.remove_face_of_list_exp)
        self.pushButton_Guardar.clicked.connect(self.save_expand)

    def remove_simplex_exp(self):
        list_items = self.list_simplex.selectedItems()
        self.expand = None
        if list_items:
            self.list_simplex.clear()
            self.simplex.clear()
            self.tableWidget_2.setRowCount(0)

    def add_simplex_exp(self):
        if self.list_simplex.count() == 2:
            crear_mensaje_error("Ya tienes una pareja introducida", "Expansión")
            return
        dim = int(self.text_dim_sim.text())
        sim_faces = set([x for x in self.faces if x is not None])
        sigma = None
        if self.simplex:
            sigma = next(x for x in self.simplex)
        if sigma is not None and sigma not in self.faces:
            crear_mensaje_error("Sigma debe ser cara de tau", "Expansión")
            return
        repetido = None
        if dim > 0 and dim == len(self.faces) - 1:
            nombre_sim = generate_sim_name(sim_faces)
        else:
            nombre_sim = self.text_nombre_sim.text()
            repetido = Aux.get_sim_by_name(self.sc.simplex, nombre_sim)
        if dim != len(self.faces) - 1 and dim != 0:
            crear_mensaje_error("Las caras del símplice no son válidas para su dimensión", "Caras Símplice")
            return
        elif repetido is not None:
            crear_mensaje_error('Ya existe un vértice con ese nombre', "Nombre Símplice")
            self.text_nombre_sim.clear()
            return
        elif not nombre_sim:
            crear_mensaje_error('Introduzca el nombre del vértice', "Nombre Símplice")
            return
        elif not nombre_sim.isalnum():
            crear_mensaje_error('El nombre contiene caracteres inválidos', "Nombre Símplice")
            return
        sim = Simplex(nombre_sim, dim)
        if sim_faces and any(elem.faces == sim_faces for elem in self.simplex):
            crear_mensaje_error("Ya existe un símplice con esas caras", "Caras Símplice")
        else:
            sim.set_faces(sim_faces)
            self.simplex.append(sim)
            self.list_simplex.addItem(str(sim))
            if self.list_simplex.count() == 2:
                self.rellenar_tabla_exp()
            self.text_nombre_sim.setText("")
            self.text_dim_sim.setValue(0)
            self.faces = list()
            self.list_faces.clear()

    def rellenar_tabla_exp(self):
        facet = self.simplex[1]
        sigma = self.simplex[0]
        sc_cloned = copy.deepcopy(self.sc)
        if self.sc.can_expand(sigma, facet):
            self.expand = sc_cloned.expand(sigma, facet)
        else:
            QMessageBox.information(self, "Error",
                                    "El complejo simplicial no puede expandirse con la pareja proporcionada")
            self.list_simplex.clear()
            return
        self.tableWidget_2.setRowCount(0)
        for i, sim in enumerate(self.expand.simplex):
            numRows = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(numRows)
            self.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
            self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
            if sim.faces:
                faces_str = "["
                for j, elem in enumerate(sim.faces):
                    faces_str = faces_str + elem.name
                    if j != len(sim.faces) - 1:
                        faces_str += ","
                faces_str += "]"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(faces_str)
                text_scrolleable.setReadOnly(True)
                self.tableWidget_2.setCellWidget(i, 2, text_scrolleable)

    def add_posible_faces_exp(self):
        self.posible_faces.clear()
        self.list_faces.clear()
        self.faces.clear()
        try:
            self.posible_faces.disconnect()
        except Exception:
            pass
        dim = int(self.text_dim_sim.text())
        if dim > 0:
            self.text_nombre_sim.setEnabled(False)
            self.text_nombre_sim.clear()
            self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(50, 50, 50);")
            all_simplex = self.sc.simplex.copy()
            if self.simplex is not None:
                all_simplex.extend(self.simplex)
            list_posible_faces = Aux.list_simplex_by_dim(all_simplex, dim - 1)
            list_posible_faces = [elem.name for elem in list_posible_faces]
            self.posible_faces.addItems(list_posible_faces)
            self.posible_faces.currentIndexChanged.connect(self.add_face_to_list_exp)
        else:
            self.text_nombre_sim.setEnabled(True)
            self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(177, 177, 177);")

    def add_face_to_list_exp(self):
        face = self.posible_faces.currentText()
        repetido = self.list_faces.findItems(face, QtCore.Qt.MatchExactly)
        dim = int(self.text_dim_sim.text()) if self.text_dim_sim.text() else 0
        if self.list_faces.count() == dim + 1:
            crear_mensaje_error("El símplice ha alcanzado el máximo de caras posible", "Caras Símplice")
        elif not repetido:
            all_simplex = self.sc.simplex.copy()
            if self.simplex is not None:
                all_simplex.extend(self.simplex)
            sim = Aux.get_sim_by_name(all_simplex, face)
            self.faces.append(sim)
            self.list_faces.addItem(face)

    def remove_face_of_list_exp(self):
        list_items = self.list_faces.selectedItems()
        if list_items:
            for elem in list_items:
                all_simplex = self.sc.simplex.copy()
                if self.simplex is not None:
                    all_simplex.extend(self.simplex)
                self.list_faces.takeItem((self.list_faces.row(elem)))
                sim_text = elem.text()
                sim = Aux.get_sim_by_name(all_simplex, sim_text)
                self.faces.remove(sim)

    def rellenar_combo_tau_colapso(self):
        facets_names = [x.name for x in self.sc.facets]
        self.combo_tau.addItems(facets_names)
        self.combo_sigma.addItems([""])
        self.combo_tau.setCurrentIndex(-1)
        self.combo_tau.currentIndexChanged.connect(self.rellenar_combo_sigma_colapso)

    def rellenar_combo_sigma_colapso(self):
        try:
            self.combo_sigma.currentIndexChanged.disconnect(self.rellenar_tabla_colapso)
        except:
            pass
        self.combo_sigma.clear()
        facet_name = self.combo_tau.currentText()
        self.combo_sigma.clear()
        facet = next(x for x in self.sc.facets if x.name == facet_name)
        faces_names = [x.name for x in facet.faces]
        self.combo_sigma.addItems(faces_names)
        self.combo_sigma.currentIndexChanged.connect(self.rellenar_tabla_colapso)

    def rellenar_tabla_colapso(self):
        facet_name = self.combo_tau.currentText()
        facet = next(x for x in self.sc.facets if x.name == facet_name)
        sigma_name = self.combo_sigma.currentText()
        sigma = next(x for x in self.sc.simplex if x.name == sigma_name)
        sc_cloned = copy.deepcopy(self.sc)
        if sc_cloned.can_collapse(sigma, facet):
            self.colapso = sc_cloned.collapse(sigma, facet)
            self.table_colapso.setRowCount(0)
            for i, sim in enumerate(self.colapso.simplex):
                numRows = self.table_colapso.rowCount()
                self.table_colapso.insertRow(numRows)
                self.table_colapso.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
                self.table_colapso.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
                if sim.faces:
                    faces_str = "["
                    for j, elem in enumerate(sim.faces):
                        faces_str = faces_str + elem.name
                        if j != len(sim.faces) - 1:
                            faces_str += ","
                    faces_str += "]"
                    text_scrolleable = QTextEdit()
                    text_scrolleable.setText(faces_str)
                    text_scrolleable.setReadOnly(True)
                    self.table_colapso.setCellWidget(i, 2, text_scrolleable)
        else:
            QMessageBox.information(self, "Error",
                                    "La pareja seleccionada no puede colapsar")

    def save_expand(self):
        if self.expand is not None:
            nombre = self.line_cone_name.text()
            edit = False
            if not nombre:
                crear_mensaje_error('Introduzca el nombre', "Nombre vacío")
            elif nombre_invalido(nombre):
                QMessageBox.information(self, "Error",
                                        "El nombre contiene caracteres inválidos")
                self.lineEdit.clear()
            else:
                edit = False
                all_sc = list_simplicial_complexes()
                if any(x for x in all_sc if x.name == nombre and x.name != self.lineEdit.text()):
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
                self.expand.name = nombre
                if edit:
                    edit_simplicial_complex(self.expand)
                else:
                    add_simplicial_complex(self.expand)
                QMessageBox.information(self, "Éxito",
                                        "Operación completada con éxito")
                self.clear_layout_dinamico(self.gridLayout_dinamico)
        else:
            QMessageBox.information(self, "Error",
                                    "No se ha calculado ningún colapso")

    def save_colapso(self):
        if self.colapso is not None:
            nombre = self.line_cone_name.text()
            edit = False
            if not nombre:
                crear_mensaje_error('Introduzca el nombre', "Nombre vacío")
            elif nombre_invalido(nombre):
                QMessageBox.information(self, "Error",
                                        "El nombre contiene caracteres inválidos")
                self.lineEdit.clear()
            else:
                edit = False
                all_sc = list_simplicial_complexes()
                if any(x for x in all_sc if x.name == nombre and x.name != self.lineEdit.text()):
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
                self.colapso.name = nombre
                if edit:
                    edit_simplicial_complex(self.colapso)
                else:
                    add_simplicial_complex(self.colapso)
                QMessageBox.information(self, "Éxito",
                                        "Operación completada con éxito")
                self.clear_layout_dinamico(self.gridLayout_dinamico)
        else:
            QMessageBox.information(self, "Error",
                                    "No se ha calculado ningún colapso")

    def set_join_ui(self):
        self.label_join.setText("Join de " + self.sc.name)
        self.label_omega_join.setText("")
        self.label_dimension_join.setText("")
        scs = list_simplicial_complexes()
        other_scs_names = [x.name for x in scs if x.name != self.sc.name]
        self.combo_join.addItems(other_scs_names)

    def compute_join(self):
        name_l = self.combo_join.currentText()
        sc_l = get_simplicial_complex(name_l)
        n_vertex_l = Aux.get_num_simplex_by_dim(sc_l.simplex, 0)
        vertex_l = sc_l.simplex[:n_vertex_l]
        if any(x for x in vertex_l if x in self.sc.simplex):
            QMessageBox.information(self, "Error",
                                    "No puede haber vértices coincidentes entre los complejos simpliciales de un join")
        else:
            self.join = join(self.sc, sc_l)
            self.label_join.setText("Join de " + self.sc.name + " con " + name_l)
            self.label_omega_join.setText(str(self.join.omega))
            self.label_dimension_join.setText(str(self.join.dimension))
            self.rellenar_tabla_join()

    def rellenar_combo_sim_stlk(self, combo):
        nombres_sim = [x.name for x in self.sc.simplex if x.dimension == 0]
        combo.addItems(nombres_sim)

    def reset_listWidget(self, list):
        list.addItem("")

    def rellenar_tabla_star(self):
        sim_name = self.comboBox_sim_star.currentText()
        sim = Aux.get_sim_by_name(self.sc.simplex, sim_name)
        star = self.sc.star(sim)
        star.sort(key=lambda x: (x.dimension, x.name))
        self.list_sim_star.clear()
        for elem in star:
            self.list_sim_star.addItem(str(elem))
        self.star = star

    def rellenar_tabla_link(self):
        sim_name = self.comboBox_sim_link.currentText()
        sim = Aux.get_sim_by_name(self.sc.simplex, sim_name)
        link = self.sc.link(sim)
        link.sort(key=lambda x: (x.dimension, x.name))
        self.list_sim_link.clear()
        for elem in link:
            self.list_sim_link.addItem(str(elem))
        self.link = link

    def rellenar_tabla_cono(self):
        self.tableWidget_2.setRowCount(0)
        for i, sim in enumerate(self.sc_cone.simplex):
            numRows = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(numRows)
            self.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
            self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
            if sim.faces:
                faces_str = "["
                for j, elem in enumerate(sim.faces):
                    faces_str = faces_str + elem.name
                    if j != len(sim.faces) - 1:
                        faces_str += ","
                faces_str += "]"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(faces_str)
                text_scrolleable.setReadOnly(True)
                self.tableWidget_2.setCellWidget(i, 2, text_scrolleable)

    def rellenar_tabla_join(self):
        self.table_join.setRowCount(0)
        for i, sim in enumerate(self.join.simplex):
            numRows = self.table_join.rowCount()
            self.table_join.insertRow(numRows)
            self.table_join.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
            self.table_join.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
            if sim.faces:
                faces_str = "["
                for j, elem in enumerate(sim.faces):
                    faces_str = faces_str + elem.name
                    if j != len(sim.faces) - 1:
                        faces_str += ","
                faces_str += "]"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(faces_str)
                text_scrolleable.setReadOnly(True)
                self.table_join.setCellWidget(i, 2, text_scrolleable)

    def save_star(self):
        if self.star is not None:
            nombre = self.lineEdit.text()
            edit = False
            if not nombre:
                crear_mensaje_error('Introduzca el nombre', "Nombre vacío")
            elif nombre_invalido(nombre):
                QMessageBox.information(self, "Error",
                                        "El nombre contiene caracteres inválidos")
                self.lineEdit.clear()
            else:
                edit = False
                all_sc = list_simplicial_complexes()
                if any(x for x in all_sc if x.name == nombre and x.name != self.lineEdit.text()):
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
                star = SimplicialComplex(nombre, Aux.get_num_simplex_by_dim(self.star, 0), self.star.copy())
                if edit:
                    edit_simplicial_complex(star)
                else:
                    add_simplicial_complex(star)
                QMessageBox.information(self, "Éxito",
                                        "Operación completada con éxito")
                self.clear_layout_dinamico(self.gridLayout_dinamico)
        else:
            QMessageBox.information(self, "Error",
                                    "No ha seleccionado ningún símplice")

    def save_link(self):
        if self.link is not None:
            nombre = self.lineEdit.text()
            edit = False
            if not nombre:
                crear_mensaje_error('Introduzca el nombre', "Nombre vacío")
            elif nombre_invalido(nombre):
                QMessageBox.information(self, "Error",
                                        "El nombre contiene caracteres inválidos")
                self.lineEdit.clear()
            else:
                edit = False
                all_sc = list_simplicial_complexes()
                if any(x for x in all_sc if x.name == nombre and x.name != self.lineEdit.text()):
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
                link = SimplicialComplex(nombre, Aux.get_num_simplex_by_dim(self.link, 0), self.link.copy())
                if edit:
                    edit_simplicial_complex(link)
                else:
                    add_simplicial_complex(link)
                QMessageBox.information(self, "Éxito",
                                        "Operación completada con éxito")
                self.clear_layout_dinamico(self.gridLayout_dinamico)
        else:
            QMessageBox.information(self, "Error",
                                    "No ha seleccionado ningún símplice")

    def save_cone(self):
        nombre = self.line_cone_name.text()
        edit = False
        if not nombre:
            crear_mensaje_error('Introduzca el nombre del cono', "Nombre vacío")
        elif nombre_invalido(nombre):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.line_cone_name.clear()
        else:
            edit = False
            all_sc = list_simplicial_complexes()
            if any(x for x in all_sc if x.name == nombre and x.name != self.label_nombre_sc.text()):
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
            self.sc_cone.name = nombre
            if edit:
                edit_simplicial_complex(self.sc_cone)
            else:
                add_simplicial_complex(self.sc_cone)
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.clear_layout_dinamico(self.gridLayout_dinamico)

    def save_join(self):
        nombre = self.line_join_name.text()
        edit = False
        if not nombre:
            crear_mensaje_error('Introduzca el nombre del join', "Nombre vacío")
        elif nombre_invalido(nombre):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.line_join_name.clear()
        else:
            edit = False
            all_sc = list_simplicial_complexes()
            if any(x for x in all_sc if x.name == nombre and x.name != self.label_nombre_sc.text()):
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
            self.join.name = nombre
            if edit:
                edit_simplicial_complex(self.join)
            else:
                add_simplicial_complex(self.join)
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.clear_layout_dinamico(self.gridLayout_dinamico)


    def rellenar_tablas_vf_auto(self):
        self.tablePairs.setRowCount(0)
        self.table_vf.setRowCount(0)
        for i, pair in enumerate(self.vf_auto.pairs_added):
            numRows = self.tablePairs.rowCount()
            self.tablePairs.insertRow(numRows)
            self.tablePairs.setItem(i, 0, QtWidgets.QTableWidgetItem("Nombre: " + pair[0].name + ", Dimensión: "
                                                                     + str(pair[0].dimension)))
            self.tablePairs.setItem(i, 1, QtWidgets.QTableWidgetItem("Nombre: " + pair[1].name + ", Dimensión: "
                                                                     + str(pair[1].dimension)))
        for i, key in enumerate(self.vf_auto.routes.keys()):
            numRows = self.table_vf.rowCount()
            self.table_vf.insertRow(numRows)
            self.table_vf.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            rutas_str = "("
            for j, rutas in enumerate(self.vf_auto.routes[key]):
                rutas_str += rutas
                if j != len(self.vf_auto.routes[key]) - 1:
                    rutas_str += ","
            rutas_str += ")"
            self.table_vf.setItem(i, 1, QtWidgets.QTableWidgetItem(rutas_str))


    def rellenar_datos_vf(self):
        self.table_vf.setRowCount(0)
        vf_name = self.comboBox_vf.currentText()
        elem = next(x for x in self.sc.vector_fields if x.name == vf_name)
        self.label_vf_name.setText(vf_name)
        for i, key in zip(range(len(elem.routes)), elem.routes.keys()):
            numRows = self.table_vf.rowCount()
            self.table_vf.insertRow(numRows)
            self.table_vf.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            rutas_str = "("
            for j, rutas in enumerate(elem.routes[key]):
                rutas_str += rutas
                if j != len(elem.routes[key]) - 1:
                    rutas_str += ","
            rutas_str += ")"
            self.table_vf.setItem(i, 1, QtWidgets.QTableWidgetItem(rutas_str))


    def guardar_vf_auto(self):
        nombre = self.line_vf_name.text()
        edit = False
        if not nombre:
            crear_mensaje_error('Introduzca el nombre del campo de vectores', "Campo de Vectores")
        elif nombre_invalido(nombre):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.text_sc_name.clear()
        else:
            if any(x for x in self.sc.vector_fields if x.name == nombre):
                box = QtWidgets.QMessageBox()
                box.setIcon(QtWidgets.QMessageBox.Question)
                box.setWindowTitle('GUARDAR')
                box.setText('Ya existe un Campo de vectores con ese nombre \r\n ¿Deseas sobreescribirlo?')
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
            self.vf_auto.name = nombre
            if edit:
                vf_to_remove = next((x for x in self.sc.vector_fields if x.name == nombre), None)
                self.sc.vector_fields.remove(vf_to_remove)
                self.sc.add_vector_field(self.vf_auto)
            else:
                self.sc.add_vector_field(self.vf_auto)
            edit_simplicial_complex(self.sc)
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.clear_layout_dinamico(self.gridLayout_dinamico)


    def populate_simplex_list_mod(self, simplex):
        for sim in simplex:
            self.list_simplex.addItem(str(sim))


    def add_simplex_table(self, simplex):
        self.tableWidget.setRowCount(0)
        for i, sim in enumerate(simplex):
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(sim.name))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sim.dimension)))
            if sim.faces:
                faces_str = "["
                for j, elem in enumerate(sim.faces):
                    faces_str = faces_str + elem.name
                    if j != len(sim.faces) - 1:
                        faces_str += ","
                faces_str += "]"
                text_scrolleable = QTextEdit()
                text_scrolleable.setText(faces_str)
                text_scrolleable.setReadOnly(True)
                if i % 2 != 0:
                    text_scrolleable.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.tableWidget.setCellWidget(i, 2, text_scrolleable)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


    def update_sc(self):
        nombre_sc = self.text_sc_name.text()
        if not nombre_sc:
            crear_mensaje_error('Introduzca el nombre del complejo simplicial', "Complejo Simplicial")
        elif nombre_invalido(nombre_sc):
            crear_mensaje_error('El nombre contiene caracteres inválidos', "Cuidado")
            self.text_sc_name.clear()
        else:
            edit = False
            all_sc = list_simplicial_complexes()
            if any(x for x in all_sc if x.name == nombre_sc and x.name != self.label_nombre_sc.text()):
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
            puntos = Aux.get_num_simplex_by_dim(self.simplex, 0)
            sc = SimplicialComplex(nombre_sc, puntos, self.simplex)
            if edit:
                edit_simplicial_complex(sc)
                remove_simplicial_complex(self.label_nombre_sc.text())
            elif sc.name != self.label_nombre_sc.text():
                remove_simplicial_complex(self.label_nombre_sc.text())
                add_simplicial_complex(sc)
            else:
                update_simplicial_complex(sc)
            self.simplex.clear()
            self.faces.clear()
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.set_sc(sc)


    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.text_nombre_sim:
            if event.key() == QtCore.Qt.Key_Return and self.text_nombre_sim.hasFocus():
                self.add_simplex()
        return super().eventFilter(obj, event)


    def add_face_to_list(self):
        face = self.posible_faces.currentText()
        repetido = self.list_faces.findItems(face, QtCore.Qt.MatchExactly)
        dim = int(self.text_dim_sim.text()) if self.text_dim_sim.text() else 0
        if self.list_faces.count() == dim + 1:
            crear_mensaje_error("El símplice ha alcanzado el máximo de caras posible", "Caras Símplice")
        elif not repetido:
            sim = Aux.get_sim_by_name(self.simplex, face)
            self.faces.append(sim)
            self.list_faces.addItem(face)


    def remove_face_of_list(self):
        list_items = self.list_faces.selectedItems()
        if list_items:
            for elem in list_items:
                self.list_faces.takeItem((self.list_faces.row(elem)))
                sim_text = elem.text()
                sim = Aux.get_sim_by_name(self.simplex, sim_text)
                self.faces.remove(sim)


    def add_posible_faces(self):
        self.posible_faces.clear()
        self.list_faces.clear()
        self.faces.clear()
        try:
            self.posible_faces.disconnect()
        except Exception:
            pass
        dim = int(self.text_dim_sim.text())
        if dim > 0:
            self.text_nombre_sim.setEnabled(False)
            self.text_nombre_sim.clear()
            self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(50, 50, 50);")
            list_posible_faces = Aux.list_simplex_by_dim(self.simplex, dim - 1)
            list_posible_faces = [elem.name for elem in list_posible_faces]
            self.posible_faces.addItems(list_posible_faces)
            self.posible_faces.currentIndexChanged.connect(self.add_face_to_list)
        else:
            self.text_nombre_sim.setEnabled(True)
            self.text_nombre_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                               "background-color: rgb(177, 177, 177);")


    def add_simplex(self):
        dim = int(self.text_dim_sim.text())
        sim_faces = set([x for x in self.faces if x is not None])
        repetido = None
        if dim > 0 and dim == len(self.faces) - 1:
            nombre_sim = generate_sim_name(sim_faces)
        else:
            nombre_sim = self.text_nombre_sim.text()
            repetido = Aux.get_sim_by_name(self.simplex, nombre_sim)
        if dim != len(self.faces) - 1 and dim != 0:
            crear_mensaje_error("Las caras del símplice no son válidas para su dimensión", "Caras Símplice")
            return
        elif repetido is not None:
            crear_mensaje_error('Ya existe un vértice con ese nombre', "Nombre Símplice")
            return
        elif not nombre_sim:
            crear_mensaje_error('Introduzca el nombre del vértice', "Nombre Símplice")
            return
        sim = Simplex(nombre_sim, dim)
        if sim_faces and any(elem.faces == sim_faces for elem in self.simplex):
            crear_mensaje_error("Ya existe un símplice con esas caras", "Caras Símplice")
        else:
            sim.set_faces(sim_faces)
            self.simplex.append(sim)
            self.list_simplex.addItem(str(sim))
            self.text_nombre_sim.setText("")
            self.text_dim_sim.setValue(0)
            self.faces = list()
            self.list_faces.clear()


    def remove_simplex(self):
        list_items = self.list_simplex.selectedItems()
        if list_items:
            for elem in list_items:
                self.list_simplex.takeItem((self.list_simplex.row(elem)))
                sim_text = elem.text()
                sim_text = sim_text.split(',', 1)[1]
                sim = Aux.get_sim_by_name(self.simplex, sim_text[9:])
                star = SimplicialComplex("", Aux.get_num_simplex_by_dim(self.simplex, 0), self.simplex).star(sim)
                self.simplex = [x for x in self.simplex if x not in star]
                for star_sim in star:
                    self.delete_from_list_simplex(str(star_sim))


    def delete_from_list_simplex(self, name_to_remove):
        items_to_remove = self.list_simplex.findItems(name_to_remove, QtCore.Qt.MatchExactly)
        for item in items_to_remove:
            row = self.list_simplex.row(item)
            self.list_simplex.takeItem(row)


    def clear_layout_dinamico(self, layout):
        self.reset_objects()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                    child.widget().setParent(None)
                else:
                    self.clear_layout_dinamico(child.layout())
        self.horizontalLayout.takeAt(1)

    def set_MenuBF(self, menu_bf):
        self.menu_bf = menu_bf

    def open_nuevo_sc(self):
        self.window_nuevo_sc = NuevoSC(self)
        self.window_nuevo_sc.show()
        self.hide()

    def open_listar_sc(self):
        self.window_listar_sc = ListarSC(self, self, self.menu_bf)
        self.window_listar_sc.show()
        self.hide()

    def open_nuevo_bf(self):
        self.window_nuevo_bf = NuevoBF(self)
        self.window_nuevo_bf.show()
        self.hide()

    def open_listar_bf(self):
        self.window_listar_bf = ListarBF(self, self.menu_bf, self)
        self.window_listar_bf.show()
        self.hide()

    def open_nuevo_vf(self):
        self.window_nuevo_vf = NuevoVF(self, self.sc)
        self.window_nuevo_vf.show()
        self.hide()
        self.clear_layout_dinamico(self.gridLayout_dinamico)

    def reset_objects(self):
        self.expand = None
        self.colapso = None
        self.join = None
        self.link = None
        self.star = None
        self.sc_cone = None
        self.vf_auto = None
        self.bf_tra = None
        self.faces.clear()
        self.simplex.clear()


class AligDelegate(QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QItemDelegate.paint(self, painter, option, index)
