from __future__ import annotations

import sys

from view import View
from interpeter import Interpeter

from PyQt5 import QtWidgets
from pynput.keyboard import Listener as keyboard
from pynput.mouse import Listener as mouse


class Listener():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.view = View(self.main_window)
        self.intrepter = Interpeter(self.main_window)

        self.keyboard = keyboard(on_press=self.intrepter.on_keyboard_press,
                                 on_release=self.intrepter.on_keyboard_release)

        self.mouse = mouse(on_click=self.intrepter.on_mouse_click)

        self.keyboard.start()
        self.mouse.start()
        self.app.exec_()
        self.keyboard.join()
        self.mouse.join()
