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
MAX_PREVIEW = 60


class Label(QtWidgets.QLabel):
    def __init__(self, text):
        super().__init__()
        super(QtWidgets.QLabel).__init__()
        self.content = text

        text = text.strip().replace("\n", "").replace("\t", "")

        if len(text) > MAX_PREVIEW:
            text = text[:MAX_PREVIEW] + "..."
        self.setText(text)

        self.mousePressEvent = self.paste
        self.setStyleSheet("""
                           QLabel::hover{
                                border: 3px;
                                border-style: solid;
                                border-color : lightblue;
                                background: lightblue;
                                border-radius: 25px;
                            }
                           """)

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

        self.cursor = QtGui.QCursor()
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
                                           QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)

        self.container.addItem(compressor)

        self.setCentralWidget(self.widget)
        self.setGeometry(600, 100, 1000, 900)

    def __clear_container(self) -> None:
        while self.content.count():
            item = self.content.takeAt(0)
            self.content.removeItem(item)
            item.widget().deleteLater()

    def show_window(self) -> None:
        x = self.cursor.pos().x()
        y = self.cursor.pos().y()
        self.move(x, y)
        self.show()

    def hide_window(self) -> None:
        self.hide()

    def refresh_clipboard(self, clipboard: list[str]) -> None:
        self.__clear_container()

        for element in clipboard:
            label = Label(element)
            self.content.addWidget(label)
