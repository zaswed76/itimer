import os
import sys
from PyQt5 import QtWidgets
from itimer.config import Config
# ROOT = os.path.join(os.path.dirname(__file__))

STYLE_PATH = "style/style.qss"
CFG_PATH = "etc/cfg.json"



class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.cfg = Config()
        self.cfg.load(CFG_PATH)
        self.data = self.cfg.data

    def closeEvent(self, event):
        pass
        self.cfg.save(CFG_PATH, self.data)
        # event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("style/style.qss", "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())