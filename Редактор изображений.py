from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('редактор.ui', self)
        self.img = None
        self.pix = None
        self.x = 0
        self.y = 0
        self.name = ''
        self.text = 'Ошибка :('
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 871, 775)
        self.setStyleSheet("QWidget { background-color: #ecffb3}")
        self.pushButton_6.clicked.connect(self.sh)
        self.blue.clicked.connect(self.one_only)
        self.green.clicked.connect(self.one_only)
        self.red.clicked.connect(self.one_only)
        self.getback.clicked.connect(self.sh)
        self.right.clicked.connect(self.rotate_right)
        self.left.clicked.connect(self.rotate_left)

    def sh(self):
        self.name = self.lineEdit.text()
        self.label_3.setText('')
        try:
            pixmap = QPixmap(self.name)
            self.label_2.setPixmap(pixmap.scaled(500, 500))
            self.img = Image.open(self.name)
            self.img.save(self.name)
        except Exception as e:
            self.label_3.setText(self.text)

    def one_only(self):
        flag = False
        if not flag:
            self.pix = self.img.load()
            self.x, self.y = self.img.size
        sender = self.sender()
        if self.label_3.text() == '':
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = self.pix[i, j]
                    if sender == self.blue:
                        r, g = 0, 0
                    elif sender == self.green:
                        r, b = 0, 0
                    elif sender == self.red:
                        g, b = 0, 0
                    self.pix[i, j] = r, g, b
            self.img.save('new_pic.jpg')
            self.disp()

    def disp(self):
        pixm = QPixmap('new_pic.jpg')
        self.label_2.setPixmap(pixm.scaled(500, 500))

    def rotate_left(self):
        try:
            self.img.transpose(Image.ROTATE_90).save('new_pic.jpg')
            self.img = Image.open('new_pic.jpg')
            self.pix = self.img.load()
            self.disp()
        except Exception as e:
            self.label_3.setText(self.text)

    def rotate_right(self):
        try:
            self.img.transpose(Image.ROTATE_270).save('new_pic.jpg')
            self.img = Image.open('new_pic.jpg')
            self.pix = self.img.load()
            self.disp()
        except Exception as e:
            self.label_3.setText(self.text)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
