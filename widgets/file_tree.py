

from pathlib import Path

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Tree
from textual.widgets.tree import TreeNode

from repository.base_folder_repository import BaseFolderRepository
from repository.base_note_repository import BaseNoteRepository


class FileTreeWidget(VerticalScroll):
    _tree: Tree

    def __init__(self, folder_repo: BaseFolderRepository, node_repo: BaseNoteRepository, *args, **kwargs) -> None:
        self._folder_repo = folder_repo
        self._node_repo = node_repo
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        self._tree = Tree("Directory")
        yield self._tree

    def on_mount(self):
        root = self.query_one(Tree).root
        root.data = Path("data")
        root.expand()

    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        node: TreeNode[Path] = event.node
        node.remove_children()
        path = node.data if node.data else ""
        folders = self._folder_repo.get_folder_by_path(Path(path))
        for folder in folders:
            node.add(folder.name, folder.path)

        notes = self._node_repo.get_notes_by_path(Path(path))
        for note in notes:
            node.add_leaf(note.name, note.path)
