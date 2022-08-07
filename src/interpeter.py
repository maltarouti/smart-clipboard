from __future__ import annotations
from typing import List

from view import View

from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.mouse import Button


class Interpeter():
    def __init__(self, view: View) -> None:
        self.view = view
        self.sequence: List[str] = list()

    def process_sequence(self) -> None:
        pass

    def on_keyboard_press(self,
                          key: Key | KeyCode | None) -> None:
        pass

    def on_mouse_click(self,
                       x: int,
                       y: int,
                       button: Button,
                       is_down: bool) -> None:
        pass

    def show_view(self) -> None:
        pass

    def hide_view(self) -> None:
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
