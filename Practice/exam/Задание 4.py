import sys
import requests

from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.button = QPushButton()
        self.lineEdit = QLineEdit()
        self.button.clicked.connect(self.my_slot_function)
        self.setGeometry(300, 400, 1300, 400)
        lay = QVBoxLayout(self)
        lay.addWidget(self.button)
        lay.addWidget(self.lineEdit)
        lay.addWidget(self.label)

    def my_slot_function(self):
        #Нужно получить значение из ссылки и вывести в консоль
        query = self.lineEdit.text()
        response = requests.get(query)
        print(response.json())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())