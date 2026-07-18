from pathlib import Path


class DesktopScanner:
    """Scans a folder and returns all user files recursively."""

    IGNORE_FOLDERS = {
        ".git",
        "__pycache__",
        ".venv",
        "venv",
        ".idea",
        ".vscode"
    }

    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def scan(self):
        files = []

        for item in self.folder_path.rglob("*"):

            if any(folder in item.parts for folder in self.IGNORE_FOLDERS):
                continue

            if item.is_file():
                files.append(item)

        return files