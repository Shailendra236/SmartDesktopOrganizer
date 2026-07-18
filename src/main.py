from scanner.scanner import DesktopScanner
from metadata.metadata import FileMetadata
from services.categorizer import FileTypeCategorizer


def main():
    print("=" * 60)
    print("          Smart Desktop Organizer")
    print("=" * 60)

    scanner = DesktopScanner(".")
    metadata = FileMetadata()
    categorizer = FileTypeCategorizer()

    files = scanner.scan()

    print(f"\nFound {len(files)} files\n")

    for file in files:
        info = metadata.get_info(file)
        category = categorizer.get_category(info.extension)

        print(f"File Name : {info.name}")
        print(f"Category  : {category}")
        print(f"Extension : {info.extension}")
        print(f"Size      : {info.size} bytes")
        print(f"Created   : {info.created}")
        print(f"Modified  : {info.modified}")
        print(f"Location  : {info.location}")
        print("-" * 60)


if __name__ == "__main__":
    main()