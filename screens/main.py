from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from note.app import AppSettings
from repository.folder_repository import FolderRepository
from repository.note_repository import NoteRepository
from widgets.file_tree import FileTreeWidget
from widgets.note_view import NoteViewWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [("q", "quit", "Exit")]  # noqa: RUF012

    def __init__(self, settings: AppSettings, *args, **kwargs) -> None:
        self.settings = settings
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        folder_repo = FolderRepository(self.settings.data_directory)
        node_repo = NoteRepository(self.settings.data_directory)
        yield Header()
        with Horizontal():
            yield FileTreeWidget(folder_repo, node_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Note Manager"
        self.query_one(NoteViewWidget).text = "## Hi!"

    def action_quit(self):
        self.app.exit()
