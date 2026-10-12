
from abc import ABC, abstractmethod
from pathlib import Path

from domain.note import Note


class BaseNoteRepository(ABC):

    @abstractmethod
    def get_notes_by_path(self, path: Path) -> list[Note]:
        pass

    @abstractmethod
    def create_note(self, path: Path, name: str) -> Note:
        pass

    @abstractmethod
    def delete_note(self, note: Note) -> None:
        pass

    @abstractmethod
    def update_note(self, note: Note, content: str, new_name: str | None = None) -> Note:
        pass

    @abstractmethod
    def load_note(self, path: Path) -> Note:
        pass
