
from abc import ABC, abstractmethod
from pathlib import Path

from domain.folder import Folder


class BaseFolerRepository(ABC):
    @abstractmethod
    def get_all_folders(self) -> list[Folder]:
        pass

    @abstractmethod
    def get_folder_by_path(self, path: Path) -> Folder:
        pass

    @abstractmethod
    def create_folder(self, name: str) -> Folder:
        pass

    @abstractmethod
    def delete_folder(self, folder: Folder) -> None:
        pass
