import shutil
from pathlib import Path

from domain.folder import Folder
from repository.folder_repository import BaseFolderRepository


class FolderRepository(BaseFolderRepository):
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path.resolve()

    def _check_path(self, path: Path) -> None:
        path = path.resolve()
        base_path = self.base_path.resolve()

        if not path.is_relative_to(base_path):
            raise ValueError("Access outside data dir is not allowed!")

        if not path.is_dir():
            raise ValueError(f"Folder doesn't exist: {path}")

    def get_folder_by_path(self, path: Path) -> list[Folder]:
        """Get Folder"""
        path = path.resolve()

        self._check_path(path)

        folders: list[Folder] = []

        for sub_path in path.iterdir():
            if sub_path.is_dir() and not sub_path.name.startswith("."):
                folders.append(
                    Folder(
                        name=sub_path.name,
                        path=sub_path
                    )
                )
        return sorted(folders, key=lambda f: f.name)

    def create_folder(self, path: Path, name: str) -> Folder:
        """Create Folder"""
        self._check_path(path)

        if not name or "/" in name or "\\" in name:
            raise ValueError("Invalid folder name!")

        path.mkdir(parents=True, exist_ok=False)
        return Folder(name, path)

    def delete_folder(self, folder: Folder) -> None:
        """Delete Folder"""
        path = folder.path.resolve()
        self._check_path(path)

        if path == self.base_path:
            raise ValueError("Can't delete Base Path!")

        shutil.rmtree(path)
