
from abc import ABC, abstractmethod
from pathlib import Path

from domain.folder import Folder


class BaseFolderRepository(ABC):

    @abstractmethod
    def get_folder_by_path(self, path: Path) -> list[Folder]:
        pass

    @abstractmethod
    def create_folder(self, path: Path, name: str) -> Folder:
        pass

    @abstractmethod
    def delete_folder(self, folder: Folder) -> None:
        pass
