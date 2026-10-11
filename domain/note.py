

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Note:
    name: str
    path: Path
    content: str | None
    created_at: datetime | None
    updated_at: datetime | None

    def __post_init__(self):
        if not self.name or self.name.strip() == "":
            raise ValueError("Note must have name!")
