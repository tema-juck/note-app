
import html2text
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from domain.note import Note
from note.app import AppSettings
from repository.base_folder_repository import BaseFolderRepository
from repository.base_note_repository import BaseNoteRepository
from screens.import_modal import ImportModal
from widgets.file_tree import FileTreeWidget
from widgets.note_view import NoteViewWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [("q", "quit", "Exit"), ("i", "import", "Import"), ("d", "delete", "Delete")]  # noqa: RUF012

    def __init__(self, settings: AppSettings, folder_repo: BaseFolderRepository,
                 node_repo: BaseNoteRepository, *args, **kwargs) -> None:
        self.settings = settings
        self._folder_repo = folder_repo
        self._node_repo = node_repo
        self._dir = settings.data_directory
        self._note: Note | None = None
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield FileTreeWidget(self._folder_repo, self._node_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Note Manager"

    def action_quit(self):
        self.app.exit()

    def action_delete(self):
        if self._note:
            self._node_repo.delete_note(self._note)
            self.query_one(FileTreeWidget).collapse()

    def action_import(self):
        self.app.push_screen(ImportModal(), self.handle_import)

    def handle_import(self, data: str | None):
        if data:
            md = html2text.html2text(data)
            self._node_repo.create_note(self._dir, "imported", md)
            self.query_one(FileTreeWidget).collapse()

    def on_file_tree_widget_note_selected(self, msg: FileTreeWidget.NoteSelected) -> None:
        note = self._node_repo.load_note(msg.node_path)
        self._note = note
        if note.content:
            self.query_one(NoteViewWidget).text = note.content
        else:
            self.query_one(NoteViewWidget).text = ""

    def on_file_tree_widget_folder_selected(self, msg: FileTreeWidget.FolderSelected) -> None:
        self._dir = msg.folder_path
