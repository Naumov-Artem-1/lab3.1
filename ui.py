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


    # Мышь

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return

        x = event.x()
        y = event.y()
        ctrl = bool(event.modifiers() & Qt.ControlModifier)

        if SELECT_ALL_UNDER_POINT:
            hits = self._storage.all_at(x, y)
        else:
            one = self._storage.topmost_at(x, y)
            hits = [one] if one is not None else []

        if not hits:
            # Клик по пустому месту.
            if not ctrl:
                self._clear_selection()
            self._storage.add(Circle(x, y))
        else:
            if ctrl:
                # Переключаем выделение у каждого попавшего.
                for c in hits:
                    c.set_selected(not c.is_selected())
            else:
                self._clear_selection()
                for c in hits:
                    c.set_selected(True)

        print("Нажатие мыши - х=",x,", y=",y, ", Ctrl=", ctrl)
        self.update()


    # Клавиатура

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            removed = self._storage.remove_selected()
            print("[Клавиатура] Delete - удалено кругов "+str(removed)+", кол элементов в хранилище "+str(len(self._storage)))
            self.update()
        else:
            super().keyPressEvent(event)

    # Отрисовка

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillRect(self.rect(), QColor("#fafafa"))

        for circle in self._storage:
            self.draw_circle(painter, circle)

        painter.end()


    def draw_circle(self, painter, circle):
        x, y, r = circle.geometry()

        if circle.is_selected():
            # Красный, сплошной, потолще.
            pen = QPen(QColor("#d32f2f"))
            pen.setWidth(3)
            pen.setStyle(Qt.SolidLine)
            painter.setPen(pen)
            painter.setBrush(QColor(211, 47, 47, 40))
        else:
            pen = QPen(QColor("#1976d2"))
            pen.setWidth(2)
            pen.setStyle(Qt.SolidLine)
            painter.setPen(pen)
            painter.setBrush(QColor(25, 118, 210, 40))

        painter.drawEllipse(x - r, y - r, r * 2, r * 2)

    def _clear_selection(self):
        for circle in self._storage:
            circle.set_selected(False)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ЛР3 - Круги на форме")
        self.resize(900, 600)
        self._paint_widget = PaintWidget()
        self.setCentralWidget(self._paint_widget)