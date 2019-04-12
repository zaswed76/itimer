

import sys
from PyQt5 import QtWidgets, QtGui


class Btn(QtWidgets.QPushButton):
    def __init__(self, parent=None, object_name="", icon_path=None, *__args):

        super().__init__(*__args)
        self.setParent(parent)
        self.setObjectName(object_name)
        self.setIcon(QtGui.QIcon(icon_path))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Btn()
    main.show()
    sys.exit(app.exec_())