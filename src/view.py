from __future__ import annotations

from PyQt5 import QtCore
from PyQt5 import QtWidgets


class View():
    def __init__(self, main_window) -> None:
        self.main_window = main_window
        main_window.setObjectName("main_window")
        main_window.resize(400, 400)
        main_window.setMinimumSize(QtCore.QSize(400, 400))
        main_window.setMaximumSize(QtCore.QSize(400, 400))

        # Hide window bar
        main_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                                   QtCore.Qt.WindowDoesNotAcceptFocus |
                                   QtCore.Qt.CustomizeWindowHint)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tool_title = QtWidgets.QLabel(self.centralwidget)
        self.tool_title.setObjectName("tool_title")
        self.horizontalLayout.addWidget(self.tool_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.copied_content = QtWidgets.QScrollArea(self.centralwidget)
        self.copied_content.setFrameShape(QtWidgets.QFrame.VLine)
        self.copied_content.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.copied_content.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.copied_content.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.copied_content.setWidgetResizable(True)
        self.copied_content.setAlignment(QtCore.Qt.AlignLeading |
                                         QtCore.Qt.AlignLeft |
                                         QtCore.Qt.AlignVCenter)

        self.copied_content.setObjectName("copied_content")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 363, 340))
        self.scrollAreaWidgetContents.setAccessibleDescription("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.copied_content.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.copied_content)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.tool_title.setText(_translate("main_window", "Clipboard"))
        self.clear_button.setText(_translate("main_window", "Clear all"))

    def show(self) -> None:
        self.main_window.show()

    def hide(self) -> None:
        self.main_window.hide()

    def refresh_clipboard(self, clipboard: list[str]) -> None:
        # TODO: Create a scrollable list
        pass

    def pin(self) -> None:
        pass

    def clear_all(self) -> None:
        pass
