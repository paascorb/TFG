from PyQt5.QtGui import QPainter, QBrush, QPen

from PyQt5.QtCore import Qt

from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class PruebaDibujo(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"

        self.top = 150

        self.left = 150

        self.width = 500

        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 8, Qt.DashLine))
        painter.drawEllipse(40, 40, 400, 400)


App = QApplication(sys.argv)

window = PruebaDibujo()

sys.exit(App.exec())
