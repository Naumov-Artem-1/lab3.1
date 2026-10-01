from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QWidget

from core import Circle, Container

SELECT_ALL_UNDER_POINT = True

class PaintWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setAutoFillBackground(True)
        self.setFocusPolicy(Qt.StrongFocus)

        self._storage = Container()


