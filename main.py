import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Okrujnost(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 650)
        self.setWindowTitle('Git и случайные окружности')

        self.button = QPushButton(self)
        self.button.resize(140, 30)
        self.button.move(400, 560)
        self.button.setText('Нарисовать окружность')
        self.button.clicked.connect(self.paint)

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
        r, g, b = randint(1, 255), randint(1, 255), randint(1, 255)
        qp.setBrush(QColor(r, g, b))
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
