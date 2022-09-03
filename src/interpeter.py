from __future__ import annotations

from view import View

from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from pynput.mouse import Button


class Interpeter():
    def __init__(self, view: View) -> None:
        self.view = view
        self.sequence: list[str] = list()
        self.cache: set[Key | KeyCode] = set()

    def __process_sequence(self) -> None:
        if len(self.cache) == 3:
            if (Key.alt in self.cache and Key.ctrl in self.cache
                    and KeyCode.from_char('e') in self.cache):

                self.view.show_window()

    def on_keyboard_press(self, key: Key | KeyCode | None) -> None:
        if (Key.alt in self.cache or Key.ctrl in self.cache
                or key == Key.alt or key == Key.ctrl):

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
        # self.view.hide_window()
        pass

    def add_element(self, text: str) -> None:
        if len(self.sequence) == 20:
            self.sequence.pop(-1)

        self.sequence.insert(0, text)
        self.view.refresh_clipboard(self.sequence)

    def remove_element(self) -> None:
        pass

    def next_element(self) -> None:
        pass

    def previous_element(self) -> None:
        pass

    def select_element(self) -> None:
        pass
