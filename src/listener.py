from __future__ import annotations

from view import View
from interpeter import Interpeter


class Listener():
    def __init__(self):
        self.view = View()
        self.intrepter = Interpeter(view=self.view)

    def initialize_listeners(self):
        # This function should initialize listeners
        pass

    def initialize_view(self):
        # This function should initialize the view
        pass
