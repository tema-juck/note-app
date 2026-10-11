"""Module CLI"""

import sys
from pathlib import Path

from config.config import AppSettings
from note.app import NoteManagerApp


def create_app(data_path: Path | None = None):
    settings: AppSettings
    if data_path:
        settings = AppSettings.from_custom_path(data_path)
    else:
        settings = AppSettings.from_defaults()

    # Start App
    return NoteManagerApp(settings)


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def letter():
    yield from "ABC"


def run():
    data_path = None
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])

    app = create_app(data_path)
    app.run()
  