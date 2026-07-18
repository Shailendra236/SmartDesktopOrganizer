from pathlib import Path
from datetime import datetime
from models.file_info import FileInfo


class FileMetadata:
    """Extract metadata from a file."""

    def get_info(self, file_path):
        file_path = Path(file_path)

        return FileInfo(
            name=file_path.name,
            extension=file_path.suffix if file_path.suffix else "No Extension",
            size=file_path.stat().st_size,
            created=datetime.fromtimestamp(
                file_path.stat().st_ctime
            ).strftime("%d-%b-%Y %I:%M %p"),
            modified=datetime.fromtimestamp(
                file_path.stat().st_mtime
            ).strftime("%d-%b-%Y %I:%M %p"),
            location=str(file_path.parent)
        )