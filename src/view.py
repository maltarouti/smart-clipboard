from __future__ import annotations

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class View():
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        main_window.setObjectName("main_window")
        main_window.resize(340, 410)
        main_window.setMinimumSize(QtCore.QSize(340, 410))
        main_window.setMaximumSize(QtCore.QSize(340, 410))

        # Hide window bar
        main_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                                   QtCore.Qt.WindowDoesNotAcceptFocus |
                                   QtCore.Qt.CustomizeWindowHint)

        self.content = QtWidgets.QWidget(main_window)
        self.content.setObjectName("content")
        self.main_widget = QtWidgets.QVBoxLayout(self.content)
        self.main_widget.setObjectName("main_widget")
        self.header = QtWidgets.QHBoxLayout()
        self.header.setObjectName("header")
        self.title = QtWidgets.QLabel(self.content)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.header.addWidget(self.title)
        self.clearall = QtWidgets.QPushButton(self.content)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clearall.setFont(font)
        self.clearall.setObjectName("clearall")
        self.header.addWidget(self.clearall)
        self.header.setStretch(0, 10)
        self.header.setStretch(1, 2)
        self.main_widget.addLayout(self.header)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)

        self.main_widget.addItem(spacerItem)
        self.clipboard = QtWidgets.QVBoxLayout()
        self.clipboard.setSpacing(6)
        self.clipboard.setObjectName("clipboard")
        self.element = QtWidgets.QHBoxLayout()
        self.element.setObjectName("element")
        self.copied_content = QtWidgets.QLabel(self.content)
        self.copied_content.setObjectName("copied_content")
        self.element.addWidget(self.copied_content)
        self.clipboard.addLayout(self.element)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)

        self.clipboard.addItem(spacerItem1)
        self.clipboard.setStretch(0, 5)
        self.clipboard.setStretch(1, 10)
        self.main_widget.addLayout(self.clipboard)
        self.main_widget.setStretch(0, 2)
        self.main_widget.setStretch(2, 10)
        main_window.setCentralWidget(self.content)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.title.setText(_translate("main_window", "Clipboard"))
        self.clearall.setText(_translate("main_window", "Clear all"))
        self.copied_content.setText(
            _translate("main_window", "Copied Content"))

    def show(self) -> None:
        self.main_window.show()

    def hide(self) -> None:
        self.main_window.hide()

    def refresh_clipboard(self, clipboard: list[str]) -> None:
        print(clipboard)
        # TODO: Create a scrollable list
        self.copied_content.setText()

    def pin(self) -> None:
        pass

    def clear_all(self) -> None:
        pass
