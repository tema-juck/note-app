from pathlib import Path

from domain.note import Note
from repository.base_note_repository import BaseNoteRepository


class NoteRepository(BaseNoteRepository):
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path.resolve()

    def _check_path(self, path: Path) -> None:
        path = path.resolve()
        base_path = self.base_path.resolve()

        if not path.is_relative_to(base_path):
            raise ValueError("Access outside data dir is not allowed!")

        if not path.is_dir():
            raise ValueError(f"Note doesn't exist: {path}")

    def get_notes_by_path(self, path: Path) -> list[Note]:
        """Get Note"""
        path = path.resolve()
        self._check_path(path)

        notes: list[Note] = []

        for sub_path in path.iterdir():
            if sub_path.is_file() and not sub_path.name.startswith(".") and sub_path.suffix == ".md":
                notes.append(
                    Note(
                        name=sub_path.name,
                        path=sub_path
                    )
                )
        return sorted(notes, key=lambda f: f.name)

    def create_note(self, path: Path, name: str, content: str) -> Note:
        """Create Note"""
        self._check_path(path)

        if not name or "/" in name or "\\" in name:
            raise ValueError("Invalid Note name!")

        new_path = path / f"{name}.md"
        new_path.write_text(content, encoding="utf-8")
        return Note(name, path)

    def delete_note(self, note: Note) -> None:
        """Delete Note"""
        path = note.path.resolve()
        path.unlink()

    def update_note(self, note: Note, content: str, new_name: str | None = None) -> Note:
        """Update Note"""
        path = note.path.resolve()
        self._check_path(path)

        path.write_text(content, encoding="utf-8")

        if new_name and new_name != note.name:
            if "/" in new_name or "\\" in new_name:
                raise ValueError("Invalid Note name")
            new_path = path.parent / f"{new_name}.md"
            path.rename(new_path)
            return Note(new_name, new_path)
        return note

    def load_note(self, path: Path) -> Note:
        with open(path, "r", encoding="utf-8") as note:
            content = note.read()
            return Note(
                path.name,
                path,
                content
            )
