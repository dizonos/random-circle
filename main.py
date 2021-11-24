import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Okrujnost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, eventt):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.flag = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(1, 300)
        qp.drawEllipse(300 - x // 2, 300 - x // 2, x, x)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Okrujnost()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
