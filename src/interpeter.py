from __future__ import annotations
from typing import Set

from PyQt5.QtWidgets import QMainWindow

from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.mouse import Button


class Interpeter():
    def __init__(self, view: QMainWindow) -> None:
        self.view = view
        print(type(self.view))
        self.cache: Set[Key | KeyCode] = set()

    def __process_sequence(self) -> None:
        if len(self.cache) == 2:
            if Key.cmd in self.cache and KeyCode.from_char('v') in self.cache:
                self.view.show()

    def on_keyboard_press(self, key: Key | KeyCode | None) -> None:
        if Key.cmd in self.cache or key == Key.cmd:
            self.cache.add(key)
            self.__process_sequence()

    def on_keyboard_release(self, key: Key | KeyCode | None) -> None:
        if key in self.cache:
            self.cache.remove(key)

    def on_mouse_click(self,
                       x: int,
                       y: int,
                       button: Button,
                       is_down: bool) -> None:
        pass

    def add_element(self) -> None:
        pass

    def remove_element(self) -> None:
        pass

    def next_element(self) -> None:
        pass

    def previous_element(self) -> None:
        pass

    def select_element(self) -> None:
        pass
