"""Modal Class"""

from textual.containers import Container, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


class ImportModal(ModalScreen[str]):
    CSS = """     
        #dialog {
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
            yield Input(placeholder="Type url for import", id="input-url")
            with Horizontal(id="buttons"):
                yield Button("Import", variant="primary", id="import-btn")
                yield Button("Cancel", id="cancel-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "import-btn":
            url_input = self.query_one("#input-url", Input)
            url = url_input.value.strip()
            if url:
                pass
            else:
                url_input.styles.border = ("solid", "red")
        else:
            self.dismiss(None)

    async def import_data(self, url: str) -> None:
        pass