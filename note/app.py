from textual.app import App

from config.config import AppSettings
from screens.main import MainScreen


class NoteManagerApp(App):
    """App"""

    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = settings

    def on_mount(self) -> None:
        """Screen"""
        main_screen = MainScreen()
        self.push_screen(main_screen)
