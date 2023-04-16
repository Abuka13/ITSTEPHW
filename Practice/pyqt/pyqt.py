import sys
import threading
import time

from PyQt6 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("window.ui", self)
        self.ui.pushButton.clicked.connect(self.start_timer)
        self.play = True
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
    def start_timer(self):
        self.play = True

        new_thread = threading.Thread(target=self.timer)
        new_thread.start()

    def timer(self):
        while self.play:
            # seconds = seconds + 1
            self.seconds += 1
            if self.seconds > 59:
                if self.minutes > 59:
                    if self.hours > 23:
                        self.hours = 0
                        self.minutes = 0
                        self.seconds = 0
                    else:
                        self.hours += 1
                        self.minutes = 0
                        self.seconds = 0
                self.minutes += 1
                self.seconds = 0
            text = f"{self.hours}:{self.minutes}" + ":" + str(self.seconds)
            # print(text)
            self.ui.labeltext.setText(text)  # Обновление (рендер) label
            time.sleep(1.0)

    def stop_timer(self):
        self.play = False
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.play = True
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        # TODO Основа

        self.setWindowTitle("proga")
        self.setGeometry(300, 400, 1300, 400)  # Ширина i t.d
        self.layout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        # TODO Надпись
        # self.main_text = QtWidgets.QLabel("Phone:",self)
        # self.main_text2 = QtWidgets.QLabel("11111111111:", self)


        # self.main_text.move(100, 100)
        # self.main_text.adjustSize()  # Настроить ширину под обьект

        self.new_text = QtWidgets.QLabel(self)


        # TODO КНОПКА
        self.button_label = QtWidgets.QLabel("Нажмите кнопку", self)
        self.layout.addWidget(self.button_label,0,0)

        self.button_start = QtWidgets.QPushButton("Запустить", self)
        self.button_start.clicked.connect(self.start_timer)
        self.layout.addWidget(self.button_start, 1, 0)

        self.label_timer = QtWidgets.QLabel("Счетчик", self)
        self.layout.addWidget(self.label_timer, 2, 0)

        self.label_text = QtWidgets.QLabel("", self)
        self.layout.addWidget(self.label_text, 3, 0)



        #TODO Позиционирование


        # self.layout.addWidget(self.main_text, 0, 0)
        # self.layout.addWidget(self.main_text2, 1, 0)


        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def start_timer(self):
        self.play = True

        new_thread = threading.Thread(target=self.timer)
        new_thread.start()

    def timer(self):
        while self.play:
            # seconds = seconds + 1
            self.seconds += 1
            if self.seconds > 59:
                if self.minutes > 59:
                    if self.hours > 23:
                        self.hours = 0
                        self.minutes = 0
                        self.seconds = 0
                    else:
                        self.hours += 1
                        self.minutes = 0
                        self.seconds = 0
                self.minutes += 1
                self.seconds = 0
            text = f"{self.hours}:{self.minutes}" + ":" + str(self.seconds)
            # print(text)
            self.label_text.setText(text)  # Обновление (рендер) label
            time.sleep(1.0)

    def stop_timer(self):
        self.play = False


    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100,50)
        self.new_text.adjustSize()


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()