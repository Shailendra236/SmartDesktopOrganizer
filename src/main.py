from scanner.scanner import DesktopScanner
from metadata.metadata import FileMetadata
from services.categorizer import FileTypeCategorizer
from services.statistics import FolderStatistics


def main():
    print("=" * 60)
    print("          Smart Desktop Organizer")
    print("=" * 60)

    scanner = DesktopScanner(".")
    metadata = FileMetadata()
    categorizer = FileTypeCategorizer()
    statistics = FolderStatistics()

    # Scan all files
    files = scanner.scan()

    print(f"\nFound {len(files)} files\n")

    # Store FileInfo objects
    file_infos = []

    for file in files:
        info = metadata.get_info(file)
        file_infos.append(info)

        category = categorizer.get_category(info.extension)

        print(f"File Name : {info.name}")
        print(f"Category  : {category}")
        print(f"Extension : {info.extension}")
        print(f"Size      : {info.size} bytes")
        print(f"Created   : {info.created}")
        print(f"Modified  : {info.modified}")
        print(f"Location  : {info.location}")
        print("-" * 60)

    # Generate statistics using FileInfo objects
    statistics.generate_statistics(file_infos)


if __name__ == "__main__":
    main()