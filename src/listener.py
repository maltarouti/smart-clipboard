from __future__ import annotations

import sys

from view import View
from interpeter import Interpeter

from PyQt5 import QtWidgets


class Listener():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.view = View(self.main_window)
        self.intrepter = Interpeter(self.view)

        # Join listeners

        self.main_window.show()
        self.app.exec_()
