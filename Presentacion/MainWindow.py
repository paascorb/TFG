import sys

from Presentacion.Listar_BF import ListarBF
from Presentacion.Listar_SC import ListarSC
from Presentacion.Main_BF import MenuBF
from Presentacion.Nuevo_BF import NuevoBF
from Presentacion.Nuevo_SC import NuevoSC
from Recursos import resources
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window_listar_bf = None
        self.window_nuevo_bf = None
        self.window_listar_sc = None
        self.window_nuevo_sc = None
        self.setWindowTitle("TFG Pablo Ascorbe")
        self.resize(750, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
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
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(250, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/flechas.png"))
        self.menubar.children()[0].setIconSize(QtCore.QSize(100, 100))
        self.menubar.children()[0].setIcon(icon)
        self.menubar.adjustSize()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 29))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuComplejo_Simplicial = QtWidgets.QMenu(self.menubar)
        self.menuComplejo_Simplicial.setFont(font)
        self.menuComplejo_Simplicial.setObjectName("menuComplejo_Simplicial")
        self.menuFunci_n_Booleana = QtWidgets.QMenu(self.menubar)
        self.menuFunci_n_Booleana.setFont(font)
        self.menuFunci_n_Booleana.setObjectName("menuFunci_n_Booleana")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setFont(font)
        self.menuAyuda.setObjectName("menuAyuda")
        self.setMenuBar(self.menubar)
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

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionNuevo_sc.triggered.connect(self.open_nuevo_sc)
        self.actionListar_sc.triggered.connect(self.open_listar_sc)
        self.actionNuevo_bf.triggered.connect(self.open_nuevo_bf)
        self.actionListar_bf.triggered.connect(self.open_listar_bf)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TFG", "TFG Pablo Ascorbe"))
        self.menuComplejo_Simplicial.setTitle(_translate("TFG", "Complejo Simplicial"))
        self.menuFunci_n_Booleana.setTitle(_translate("TFG", "Función Booleana"))
        self.menuAyuda.setTitle(_translate("TFG", "Ayuda"))
        self.actionNuevo_sc.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_sc.setShortcut(_translate("TFG", "Ctrl+N"))
        self.actionListar_sc.setText(_translate("TFG", "Cargar"))
        self.actionListar_sc.setShortcut(_translate("TFG", "Ctrl+L"))
        self.actionNuevo_bf.setText(_translate("TFG", "Nuevo"))
        self.actionNuevo_bf.setShortcut(_translate("TFG", "Ctrl+M"))
        self.actionListar_bf.setText(_translate("TFG", "Cargar"))
        self.actionListar_bf.setShortcut(_translate("TFG", "Ctrl+K"))
        self.actionAyuda.setText(_translate("TFG", "Ayuda de TFG Pablo Ascorbe"))
        self.actionAcerca.setText(_translate("TFG", "Acerca de la aplicación"))

    def open_nuevo_sc(self):
        self.window_nuevo_sc = NuevoSC(self)
        self.window_nuevo_sc.show()
        self.hide()

    def open_listar_sc(self):
        self.window_listar_sc = ListarSC(self)
        self.window_listar_sc.show()
        self.hide()

    def open_nuevo_bf(self):
        self.window_nuevo_bf = NuevoBF(self)
        self.window_nuevo_bf.show()
        self.hide()

    def open_listar_bf(self):
        menu_bf = MenuBF()
        self.window_listar_bf = ListarBF(self, menu_bf)
        self.window_listar_bf.show()
        self.hide()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
