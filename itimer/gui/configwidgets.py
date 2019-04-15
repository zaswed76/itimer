import sys
from PyQt5 import QtWidgets

class Hbox(QtWidgets.QHBoxLayout):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

    def add_widget(self, QWidget, stretch=0, Qt_Alignment=None, Qt_AlignmentFlag=None, *args, **kwargs):
        self.addWidget(QWidget)



class IntervalWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightgrey")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton("1")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn3 = QtWidgets.QPushButton("3")
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addWidget(self.btn3)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = IntervalWidget()
    main.show()
    sys.exit(app.exec_())