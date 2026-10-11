

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Tree

from repository.base_repository import BaseFolderRepository


class FileTreeWidget(VerticalScroll):
    _tree: Tree

    def __init__(self, folder_repo: BaseFolderRepository, *args, **kwargs) -> None:
        self._folder_repo = folder_repo
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        self._tree = Tree("Directory")
        yield self._tree
