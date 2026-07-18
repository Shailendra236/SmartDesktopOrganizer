class FileTypeCategorizer:
    """Categorize files based on their extensions."""

    def __init__(self):
        self.categories = {
            ".pdf": "Documents",
            ".doc": "Documents",
            ".docx": "Documents",
            ".txt": "Documents",

            ".xls": "Spreadsheets",
            ".xlsx": "Spreadsheets",
            ".csv": "Spreadsheets",

            ".jpg": "Images",
            ".jpeg": "Images",
            ".png": "Images",
            ".gif": "Images",

            ".mp4": "Videos",
            ".avi": "Videos",
            ".mkv": "Videos",

            ".mp3": "Audio",
            ".wav": "Audio",

            ".zip": "Archives",
            ".rar": "Archives",
            ".7z": "Archives",

            ".py": "Code",
            ".java": "Code",
            ".cpp": "Code",
            ".js": "Code",

            ".exe": "Applications",
            ".msi": "Applications"
        }

    def get_category(self, extension):
        """Return the category for a file extension."""

        extension = extension.lower()

        return self.categories.get(extension, "Others")