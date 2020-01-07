import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from random import randint

lst = ['Car1.png', 'Car2.png', 'Car3.png']


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.resize(300, 300)
        self.setWindowTitle('Машинка')
        self.label = QLabel(self)
        self.pixmap = 'Car1.png'
        self.label.resize(100, 50)
        self.label.move(0, 0)
        self.label.setPixmap(QPixmap(self.pixmap).scaled(100, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
                if x not in range(0, 225):
            if x > 0:
                x = 225
            elif x < 225:
                x = 0
        if y not in range(0, 250):
            if y > 0:
                y = 255
            elif y < 250:
                y = 0
        if x != self.label.x() or y != self.label.y():
            self.label.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == 32:
            l = lst[randint(0, 2)]
            while l == self.pixmap:
                l = l = lst[randint(0, 2)]
            self.pixmap = l
            self.label.setPixmap(QPixmap(self.pixmap).scaled(100, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
