from scanner.scanner import DesktopScanner


def main():
    print("=" * 50)
    print(" Smart Desktop Organizer ")
    print("=" * 50)

    scanner = DesktopScanner(".")

    files = scanner.scan()

    print(f"\nFound {len(files)} files\n")

    for file in files:
        print(f"File Name : {file.name}")
        print(f"Location  : {file.parent}")
        print(f"Extension : {file.suffix if file.suffix else 'No Extension'}")
        print(f"Size      : {file.stat().st_size} bytes")
        print("-" * 50)


if __name__ == "__main__":
    main()