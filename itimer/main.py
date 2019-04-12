import os
import sys
from PyQt5 import QtWidgets, QtGui
from itimer.config import Config
from itimer.gui import basewindow, configwindow, widgets

# ROOT = os.path.join(os.path.dirname(__file__))

STYLE_PATH = "style/style.qss"
CFG_PATH = "etc/cfg.json"
CFG_ICON_PATH = "resource/icons/cfg.png"


class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cfg = Config()
        self.cfg.load(CFG_PATH)
        self.data = self.cfg.data

        self.Centr = QtWidgets.QWidget()
        self.setCentralWidget(self.Centr)

        self.stack = QtWidgets.QStackedLayout(self.Centr)

        self.base_widget = basewindow.Widget()
        self.cfg_widget = configwindow.Widget()
        self.stack.addWidget(self.base_widget)
        self.stack.addWidget(self.cfg_widget)
        self.stack.setCurrentIndex(0)

        self.cfg_show_btn = widgets.Btn(self.base_widget,
                                   "show_cfg_btn", CFG_ICON_PATH)
        self.cfg_show_btn.clicked.connect(self.show_settings)

        self.cfg_close_btn = widgets.Btn(self.cfg_widget,
                                   "close_cfg_btn", CFG_ICON_PATH)
        self.cfg_close_btn.clicked.connect(self.close_settings)

    def show_settings(self):
        print(1)
        self.stack.setCurrentIndex(1)

    def close_settings(self):
        self.stack.setCurrentIndex(0)

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
