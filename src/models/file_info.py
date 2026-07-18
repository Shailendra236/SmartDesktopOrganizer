from dataclasses import dataclass


@dataclass
class FileInfo:
    name: str
    extension: str
    size: int
    created: str
    modified: str
    location: str