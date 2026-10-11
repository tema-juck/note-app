

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Note:
    name: str
    path: Path
    content: str | None = ""
    created_at: Optional[datetime] = datetime.now()  # noqa: RUF009, UP045
    updated_at: Optional[datetime] = datetime.now()  # noqa: RUF009, UP045

    def __post_init__(self):
        if not self.name or self.name.strip() == "":
            raise ValueError("Note must have name!")
