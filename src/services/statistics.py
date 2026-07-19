class FolderStatistics:
    """Generate statistics for scanned files."""

    def __init__(self):
        pass

    def format_size(self, size):
        """Convert bytes into a human-readable format."""

        if size < 1024:
            return f"{size} Bytes"
        elif size < 1024 ** 2:
            return f"{size / 1024:.2f} KB"
        elif size < 1024 ** 3:
            return f"{size / (1024 ** 2):.2f} MB"
        else:
            return f"{size / (1024 ** 3):.2f} GB"

    def generate_statistics(self, files, categorizer):
        """Generate statistics for a list of FileInfo objects."""

        total_files = len(files)
        total_size = 0
        category_counts = {}

        # Track largest and smallest files
        largest_file = None
        smallest_file = None

        # Calculate statistics
        for file in files:
            total_size += file.size

            # Find largest file
            if largest_file is None or file.size > largest_file.size:
                largest_file = file

            # Find smallest file
            if smallest_file is None or file.size < smallest_file.size:
                smallest_file = file

            category = categorizer.get_category(file.extension)

            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1

        # Calculate average file size
        if total_files > 0:
            average_size = total_size / total_files
        else:
            average_size = 0

        # Print statistics
        print("\n" + "=" * 60)
        print("Folder Statistics")
        print("=" * 60)
        print(f"Total Files : {total_files}")
        print(f"Total Size  : {self.format_size(total_size)}")
        print(f"Average Size: {self.format_size(average_size)}")

        print("\nCategory Summary")
        print("-" * 25)

        for category, count in category_counts.items():
            print(f"{category:<12}: {count}")

        # Print largest file
        print("\nLargest File")
        print("-" * 25)

        if largest_file:
            print(f"Name     : {largest_file.name}")
            print(f"Size     : {self.format_size(largest_file.size)}")
            print(f"Location : {largest_file.location}")

        # Print smallest file
        print("\nSmallest File")
        print("-" * 25)

        if smallest_file:
            print(f"Name     : {smallest_file.name}")
            print(f"Size     : {self.format_size(smallest_file.size)}")
            print(f"Location : {smallest_file.location}")