from textual.app import App

from config.config import AppSettings
from repository.folder_repository import FolderRepository
from repository.note_repository import NoteRepository
from screens.main import MainScreen


class NoteManagerApp(App):
    """App"""

    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = settings

    def on_mount(self) -> None:
        """Screen"""
        folder_repo = FolderRepository(self.settings.data_directory)
        node_repo = NoteRepository(self.settings.data_directory)
        main_screen = MainScreen(self.settings, folder_repo, node_repo)
        self.push_screen(main_screen)
