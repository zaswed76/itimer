import sys
from PyQt5 import QtWidgets, QtCore
from itimer.gui import configwidgets

class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: grey")
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.setContentsMargins(0, 4, 2, 0)
        self.vbox.setSpacing(0)
        self.tool_widget = QtWidgets.QFrame()
        self.tool_widget.setFixedHeight(36)
        self.vbox.addWidget(self.tool_widget, alignment=QtCore.Qt.AlignTop)

        self.select_signal = configwidgets.SignalSelectionWidget()
        self.vbox.addWidget(self.select_signal, alignment=QtCore.Qt.AlignTop)
        self.vbox.addStretch(100)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())