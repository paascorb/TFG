from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


def crear_mensaje_error(mensaje, titulo):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(mensaje)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("../Recursos/icono.ico"))
    msg.setWindowIcon(icon)
    msg.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                      "color: rgb(255, 255, 255);")
    ok_button = msg.button(QtWidgets.QMessageBox.Ok)
    ok_button.setText('Aceptar')
    ok_button.setStyleSheet("background-color: rgb(71, 71, 71)")
    msg.exec_()