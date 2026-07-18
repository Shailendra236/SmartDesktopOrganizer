from scanner.scanner import DesktopScanner
from metadata.metadata import FileMetadata


def main():
    print("=" * 60)
    print("          Smart Desktop Organizer")
    print("=" * 60)

    scanner = DesktopScanner(".")
    metadata = FileMetadata()

    files = scanner.scan()

    print(f"\nFound {len(files)} files\n")

    for file in files:
        info = metadata.get_info(file)

        print(f"File Name : {info.name}")
        print(f"Extension : {info.extension}")
        print(f"Size      : {info.size} bytes")
        print(f"Created   : {info.created}")
        print(f"Modified  : {info.modified}")
        print(f"Location  : {info.location}")
        print("-" * 60)


if __name__ == "__main__":
    main()