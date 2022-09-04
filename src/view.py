from __future__ import annotations

import pyperclip
from pynput.keyboard import Key
from pynput.keyboard import Controller

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

KEYBOARD = Controller()
SHIFT_L = Key.shift_l
INSERT = Key.insert

MAX_PREVIEW = 50


class Label(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        super(QtWidgets.QLabel).__init__()
        self.content = text

        text = text.strip()
        if len(text) > MAX_PREVIEW:
            text = text[:MAX_PREVIEW] + "..."
        self.setText(text)

        self.mousePressEvent = self.paste

    def paste(self, event: QtGui.QMouseEvent) -> None:
        pyperclip.copy(self.content)
        KEYBOARD.press(SHIFT_L)
        KEYBOARD.press(INSERT)

        KEYBOARD.release(SHIFT_L)
        KEYBOARD.release(INSERT)


class View(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Smart Clipboard")
        self.setObjectName("main_window")
        self.resize(400, 400)
        self.setMinimumSize(QtCore.QSize(400, 400))
        self.setMaximumSize(QtCore.QSize(400, 400))

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.WindowDoesNotAcceptFocus |
                            QtCore.Qt.Tool)

        self.init()

    def init(self) -> None:
        self.widget = QtWidgets.QWidget()
        self.container = QtWidgets.QVBoxLayout(self.widget)
        self.widget.setLayout(self.container)

        # Add the clipboard preview
        self.content = QtWidgets.QVBoxLayout()
        self.container.addLayout(self.content)

        # Compress them
        compressor = QtWidgets.QSpacerItem(20, 500,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)

        self.container.addItem(compressor)

        self.setCentralWidget(self.widget)
        self.setGeometry(600, 100, 1000, 900)

    def __clear_container(self) -> None:
        while self.content.count():
            item = self.content.takeAt(0)
            self.content.removeItem(item)
            item.widget().close()

    def show_window(self) -> None:
        self.show()

    def hide_window(self) -> None:
        self.hide()

    def refresh_clipboard(self, clipboard: list[str]) -> None:
        self.__clear_container()

        for element in clipboard:
            label = Label(element)
            self.content.addWidget(label)
