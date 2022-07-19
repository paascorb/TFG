from PyQt5.QtWidgets import QWidget, QItemDelegate, QTextEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import ModeloDeDominio.Auxiliary as Aux
from Persistencia.PersistenceSimplicialComplex import update_simplicial_complex

from Presentacion.Hasse import Hasse
from Presentacion.PresentacionAuxiliar import crear_mensaje_error


class NuevoVF(QWidget):
    def __init__(self, parent, sc):
        self.close_accepted = False
        self.vf = None
        self.avaliable_pairs = None
        self.hasse = None
        self.parent = parent
        super().__init__()
        self.sc = sc
        self.path_hasse = "../Recursos/Hasse.png"
        self.setObjectName("Creación Campo de Vectores")
        self.setObjectName("Form")
        if parent.isMaximized():
            self.showMaximized()
        else:
            self.resize(parent.width(), parent.height())
            self.move(parent.pos())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
        self.setWindowIcon(icon)
        self.setStyleSheet("QWidget{\n"
                           "background-color: rgb(27, 27, 27);\n"
                           "color: rgb(255, 255, 255);\n"
                           "}\n"
                           "")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, 15, 40, 15)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.tablePairs = QtWidgets.QTableWidget(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tablePairs.setFont(font)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.line_vf_name = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_vf_name.setFont(font)
        self.line_vf_name.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(177, 177, 177);")
        self.line_vf_name.setObjectName("line_vf_name")
        self.horizontalLayout_3.addWidget(self.line_vf_name)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 2)
        self.pushButton_Guardar = QtWidgets.QPushButton(self)
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
        self.gridLayout.addWidget(self.pushButton_Cancelar, 3, 2, 1, 1)
        self.pushButton_Anadir = QtWidgets.QPushButton(self)
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
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 413, 318))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout_2.addWidget(self.image, 0, 0, 2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 2, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        header = self.tablePairs.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.add_pairs_to_table()
        self.pushButton_Anadir.clicked.connect(self.add_route)
        self.tablePairs.cellDoubleClicked.connect(self.add_route)
        self.pushButton_Guardar.clicked.connect(self.guardar_vf)
        self.pushButton_Cancelar.clicked.connect(self.close)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Creación Campo de Vectores"))
        self.label_3.setText(_translate("Form", "Creación manual de un campo de vectores"))
        self.pushButton_Cancelar.setText(_translate("Form", "Cancelar"))
        item = self.tablePairs.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sigma"))
        item = self.tablePairs.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tau"))
        self.label_2.setText(_translate("Form", "Nombre:"))
        self.pushButton_Guardar.setText(_translate("Form", "Guardar"))
        self.pushButton_Anadir.setText(_translate("Form", "Añadir"))

        self.attachImage()

    def add_pairs_to_table(self):
        fblocks = self.vf.fblocks
        self.avaliable_pairs = list()
        self.tablePairs.setRowCount(0)
        for dim, elem in enumerate(fblocks):
            for source, i in zip(elem, range(0, len(elem))):
                for target, j in zip(source, range(0, len(source))):
                    if target == 1:
                        sigma = self.sc.simplex[Aux.get_sim_index(i, dim, self.sc.c_vector)]
                        tau = self.sc.simplex[Aux.get_sim_index(j, dim + 1, self.sc.c_vector)]
                        pair = (sigma, tau)
                        if all(self.vf.check_source(x) and self.vf.check_target(x) for x in pair):
                            self.avaliable_pairs.append(pair)
        for i, elem in enumerate(self.avaliable_pairs):
            numRows = self.tablePairs.rowCount()
            self.tablePairs.insertRow(numRows)
            text_sigma = elem[0].name + ", " + str(elem[0].dimension)
            text_tau = elem[1].name + ", " + str(elem[1].dimension)
            self.tablePairs.setItem(i, 0, QtWidgets.QTableWidgetItem(text_sigma))
            self.tablePairs.setItem(i, 1, QtWidgets.QTableWidgetItem(text_tau))
        self.tablePairs.setItemDelegate(AligDelegate())

    def add_route(self):
        row = self.tablePairs.currentRow()
        if row != -1:
            text_sigma = self.tablePairs.item(row, 0).text()
            text_tau = self.tablePairs.item(row, 1).text()
            text_sigma = text_sigma[:text_sigma.rindex(',')]
            text_tau = text_tau[:text_tau.rindex(',')]
            sigma = Aux.get_sim_by_name(self.sc.simplex, text_sigma)
            tau = Aux.get_sim_by_name(self.sc.simplex, text_tau)
            ciclo = self.hasse.point_up_edge(tau, sigma)
            self.vf = self.hasse.vf
            self.add_pairs_to_table()
            self.paint_image()
            if ciclo:
                self.tablePairs.setRowCount(0)
                QMessageBox.information(self, "¡Ciclo!",
                                        "Ciclo formado por: " + sigma.name + " y " + tau.name)

    def paint_image(self):
        pixMap = QtGui.QPixmap(self.path_hasse)
        self.image.setPixmap(pixMap)

    def attachImage(self):
        sc = self.sc
        self.hasse = Hasse(sc)
        self.vf = self.hasse.vf
        self.hasse.plot_hasse()
        pixMap = QtGui.QPixmap(self.path_hasse)
        self.image.setPixmap(pixMap)
        self.scrollArea.setWidgetResizable(True)
        self.image.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def guardar_vf(self):
        nombre = self.line_vf_name.text()
        repetido = any(x for x in self.sc.vector_fields if x.name == nombre)
        if not nombre:
            crear_mensaje_error('Introduzca el nombre del campo de vectores', "Campo de Vectores")
            return
        elif repetido:
            crear_mensaje_error('Ya existe un campo de vectores con ese nombre', "Campo de Vectores")
            return
        elif not nombre.isalnum():
            crear_mensaje_error('El nombre contiene caracteres no válidos', "Campo de Vectores")
            return
        else:
            self.vf.name = nombre
        self.close_accepted = True
        update_simplicial_complex(self.sc)
        QMessageBox.information(self, "Éxito",
                                "Operación completada con éxito")
        self.close()

    def closeEvent(self, event):
        if self.close_accepted:
            if self.isMaximized():
                self.parent.showMaximized()
            else:
                self.parent.show()
                self.parent.resize(self.width(), self.height())
                self.parent.move(self.pos())
            event.accept()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('SALIR')
            box.setText('¿Estás seguro que deseas salir?\r\n Se perderá el progreso')
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
                self.sc.vector_fields = self.sc.vector_fields[:-1]
                if self.isMaximized():
                    self.parent.showMaximized()
                else:
                    self.parent.show()
                    self.parent.resize(self.width(), self.height())
                    self.parent.move(self.pos())
                event.accept()
            else:
                event.ignore()


class AligDelegate(QItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        QItemDelegate.paint(self, painter, option, index)
