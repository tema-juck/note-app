from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header, Tree

from widgets.markdown import MarkdownWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [("q", "quit", "Exit")]  # noqa: RUF012

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree(label="My Base", id="tree")
            yield MarkdownWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Note Manager"
        self.query_one(MarkdownWidget).text = "## Hi!"

    def action_quit(self):
        self.app.exit()
