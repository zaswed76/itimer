import sys
import os
from PyQt5 import QtWidgets, QtCore


class OptionNameLabel(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)


class SignalSelectionWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.current_signal = ""

        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton("1")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn_choose_path = QtWidgets.QPushButton("+")
        self.btn_choose_path.clicked.connect(self.choose_path)
        self.user_signal_lb = QtWidgets.QLabel("metallica.mp3")
        self.lb = OptionNameLabel("сигнал")
        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addWidget(self.btn_choose_path)
        self.hbox.addWidget(self.user_signal_lb)

    def choose_path(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        if fname:
            self.user_signal_lb.setText(fname)
            self.data["signal_path"] = fname
        else:
            pass

class IntervalSelectionWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("интервал")
        self.interval = QtWidgets.QTimeEdit()
        self.interval.timeChanged.connect(self.time_change)
        print(self.interval.dateTime())
        self.interval.setDisplayFormat("HH:mm:ss")

        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.interval)

    def time_change(self, qtime):
        print(qtime)


class DurationSignalWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("длительность")
        self.duration = QtWidgets.QSpinBox()
        self.duration.setValue(self.data["duration"])
        self.duration.valueChanged.connect(self.value_changed)


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.duration)

    def value_changed(self, value):
        self.data["duration"] = value

class AutostartWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("автостарт")
        self.autostar = QtWidgets.QCheckBox()


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.autostar)

class SelectingCyclingWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("зациклить")
        self.cycling = QtWidgets.QCheckBox()


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.cycling)

class VolumeWidget(QtWidgets.QFrame):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("громкость")
        self.volume = QtWidgets.QSlider(QtCore.Qt.Horizontal)


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.volume)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = SignalSelectionWidget()
    main.show()
    sys.exit(app.exec_())