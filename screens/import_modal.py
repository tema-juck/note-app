"""Modal Class"""

from textual.containers import Container, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


class ImportModal(ModalScreen):
    CSS = """
        Screen {
            align: center middle;
        }
        
        #dialog {
            width: 60;
            height: 15;
            border: solid grey;
        }
        
        #title {
            dock: top;
            content-align: center middle;
            padding: 0 1;
            height: 2;
        }
        
        #buttons {
            align: center middle;
        }
    """

    def compose(self):
        with Container(id="dialog"):
            yield Static("Daten Import", id="title")
            yield Input(placeholder="Type url for import")
            with Horizontal(id="buttons"):
                yield Button("Import", variant="primary")
                yield Button("Cancel")
