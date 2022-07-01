from __future__ import annotations

from view import View


class Interpeter():
    def __init__(self, view: View):
        self.view = view
        self.sequence = list()

    def process_sequence(self) -> None:
        pass

    def on_keyboard_press(self) -> None:
        pass

    def on_mouse_click(self) -> None:
        pass

    def show_view(self) -> None:
        pass

    def hide_view() -> None:
        pass

    def add_element() -> None:
        pass

    def remove_element() -> None:
        pass

    def next_element() -> None:
        pass

    def previous_element() -> None:
        pass

    def select_element() -> None:
        pass
