from functools import reduce

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from LogicaDeNegocio.Join import *
from LogicaDeNegocio.SimplicialComplexManager import *
import ModeloDeDominio.Auxiliary as Aux
from ModeloDeDominio.SimplicialComplex import SimplicialComplex
from Presentacion.PresentacionAuxiliar import *


class NuevoSC(QWidget):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.close_accepted = False
        self.simplex = list()
        self.faces = list()

        self.setWindowTitle("Crear Complejo Simplicial")
        self.resize(750, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                           "color: rgb(255, 255, 255);")
        self.gridLayout_4 = QtWidgets.QGridLayout(self)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_Cancelar = QtWidgets.QPushButton(self)
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
        self.gridLayout_6.addWidget(self.pushButton_Cancelar, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
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
        self.gridLayout_6.addWidget(self.pushButton_Aceptar, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_QuitarSim = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_QuitarSim.sizePolicy().hasHeightForWidth())
        self.pushButton_QuitarSim.setSizePolicy(sizePolicy)
        self.pushButton_QuitarSim.setMinimumSize(QtCore.QSize(340, 25))
        self.pushButton_QuitarSim.setMaximumSize(QtCore.QSize(340, 16777215))
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
        self.gridLayout_2.addWidget(self.pushButton_QuitarSim, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.list_simplex, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 3, 1)
        self.label = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
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
        self.text_dim_sim = QtWidgets.QSpinBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_dim_sim.setFont(font)
        self.text_dim_sim.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.text_dim_sim.setObjectName("text_dim_sim")
        self.gridLayout_3.addWidget(self.text_dim_sim, 3, 1, 1, 1)
        self.posible_faces = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.posible_faces.setFont(font)
        self.posible_faces.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(177, 177, 177);")
        self.posible_faces.setObjectName("posible_faces")
        self.gridLayout_3.addWidget(self.posible_faces, 4, 1, 1, 1)
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
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.toolButton_mas = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_mas.setStyleSheet("QToolButton{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(71, 71, 71);;}\n"
                                          "\n"
                                          "QToolButton:hover{\n"
                                          "    background-color: rgb(100, 100, 100);\n"
                                          "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/mas.ico"))
        self.toolButton_mas.setIcon(icon1)
        self.toolButton_mas.setObjectName("toolButton_mas")
        self.horizontalLayout.addWidget(self.toolButton_mas)
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
        icon2.addPixmap(QtGui.QPixmap(":/images/menos.ico"))
        self.toolButton_menos.setIcon(icon2)
        self.toolButton_menos.setObjectName("toolButton_menos")
        self.horizontalLayout.addWidget(self.toolButton_menos)
        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.text_sc_name = QtWidgets.QLineEdit(self)
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
        self.gridLayout.addWidget(self.text_sc_name, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        # Aquí definiremos el orden:
        self.setTabOrder(self.text_sc_name, self.text_nombre_sim)
        self.setTabOrder(self.text_nombre_sim, self.text_dim_sim)
        self.setTabOrder(self.text_dim_sim, self.posible_faces)
        self.setTabOrder(self.posible_faces, self.pushButton_Anadir)
        self.setTabOrder(self.pushButton_Anadir, self.pushButton_Aceptar)
        self.setTabOrder(self.pushButton_Aceptar, self.pushButton_Cancelar)

        self.pushButton_Cancelar.clicked.connect(self.close)
        self.pushButton_Aceptar.clicked.connect(self.acept_and_save_form)
        self.pushButton_Anadir.clicked.connect(self.add_simplex)
        self.pushButton_QuitarSim.clicked.connect(self.remove_simplex)
        self.text_dim_sim.textChanged.connect(self.add_posible_faces)
        self.text_nombre_sim.installEventFilter(self)
        self.toolButton_mas.clicked.connect(self.add_face_to_list)
        self.toolButton_menos.clicked.connect(self.remove_face_of_list)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.text_nombre_sim:
            if event.key() == QtCore.Qt.Key_Return and self.text_nombre_sim.hasFocus():
                self.add_simplex()
        return super().eventFilter(obj, event)

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

    def is_char_list(self, lista):
        return not any(x for x in lista if len(x) > 1)

    def remove_simplex(self):
        list_items = self.list_simplex.selectedItems()
        if list_items:
            for elem in list_items:
                self.list_simplex.takeItem((self.list_simplex.row(elem)))
                sim_text = elem.text()
                sim_text = sim_text.split(',', 1)[1]
                sim = Aux.get_sim_by_name(self.simplex, sim_text[9:])
                star = SimplicialComplex("", Aux.get_num_simplex_by_dim(self.simplex, 0), self.simplex).star(sim)
                self.simplex.remove(sim)
                self.simplex = [x for x in self.simplex if x not in star]
                for star_sim in star:
                    self.delete_from_list_simplex(str(star_sim))

    def delete_from_list_simplex(self, name_to_remove):
        items_to_remove = self.list_simplex.findItems(name_to_remove, QtCore.Qt.MatchExactly)
        for item in items_to_remove:
            row = self.list_simplex.row(item)
            self.list_simplex.takeItem(row)

    def acept_and_save_form(self):
        nombre_sc = self.text_sc_name.text()
        if not nombre_sc:
            crear_mensaje_error('Introduzca el nombre del complejo simplicial', "Complejo Simplicial")
        elif nombre_invalido(nombre_sc):
            QMessageBox.information(self, "Error",
                                    "El nombre contiene caracteres inválidos")
            self.text_sc_name.clear()
        else:
            all_sc = list_simplicial_complexes()
            edit = False
            if any(x for x in all_sc if x.name == nombre_sc):
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
            else:
                add_simplicial_complex(sc)
            self.close_accepted = True
            QMessageBox.information(self, "Éxito",
                                    "Operación completada con éxito")
            self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form_Nuevo_SC", "Crear Complejo Simplicial"))
        self.pushButton_Cancelar.setText(_translate("Form_Nuevo_SC", "Cancelar"))
        self.pushButton_Aceptar.setText(_translate("Form_Nuevo_SC", "Aceptar"))
        self.groupBox.setTitle(_translate("Form_Nuevo_SC", "Símplices"))
        self.pushButton_QuitarSim.setText(_translate("Form_Nuevo_SC", "Quitar"))
        __sortingEnabled = self.list_simplex.isSortingEnabled()
        self.list_simplex.setSortingEnabled(False)
        self.list_simplex.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form_Nuevo_SC", "Nombre del Complejo simplicial:"))
        self.groupBox_2.setTitle(_translate("Form_Nuevo_SC", "Añadir Símplice"))
        self.pushButton_Anadir.setText(_translate("Form_Nuevo_SC", "Añadir"))
        self.label_4.setText(_translate("Form_Nuevo_SC", "Caras"))
        self.toolButton_mas.setText(_translate("Form_Nuevo_SC", "..."))
        self.toolButton_menos.setText(_translate("Form_Nuevo_SC", "..."))
        self.label_2.setText(_translate("Form_Nuevo_SC", "Nombre del Símplice:"))
        self.label_3.setText(_translate("Form_Nuevo_SC", "Dimensión:"))
