import sys
from typing import Mapping, Sequence

(SUCCESS, FILE_ERROR) = range(2)


def report(book_file: str) -> int:
    """Create and print a book report"""
    try:
        book_text = load_book(book_file)
    except OSError as err:
        print(f"Could not open '{book_file}'", file=sys.stderr)
        print(err)
        return FILE_ERROR

    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    report = format_report(book_file, word_count, character_count)

    print(report)
    return SUCCESS


def format_report(
    book_file: str, word_count: int, character_count: Mapping[str, int]
) -> str:
    """Produce a formatted book report."""
    report = f"--- Begin report of {book_file} ---\n"

    report += (
        f"{word_count} word{"s" if word_count != 1 else ""} found in the document\n\n\n"
    )

    sorted_characters = sort_character_count(character_count)

    for ch, count in sorted_characters:
        report += (
            f"The '{ch}' character was found {count} time{"s" if count != 1 else ""}\n"
        )

    report += "--- End report ---"

    return report


def load_book(path: str) -> str:
    """Load a book as a string."""
    with open(path) as f:
        return f.read()


def count_words(text: str) -> int:
    """Count the number of words in the given text."""
    return len(text.split())


def count_characters(text: str) -> Mapping[str, int]:
    """Count the number of times individual characters appear in the given text."""
    count: dict[str, int] = {}

    for ch in text:
        lowered = ch.lower()

        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count


def sort_character_count(
    character_count: Mapping[str, int],
) -> Sequence[tuple[str, int]]:
    """Sort the character count by frequency, returning only alphanumeric characters."""
    return sorted(
        ((ch, character_count[ch]) for ch in character_count if ch.isalpha()),
        key=lambda x: x[1],
        reverse=True,
    )


if __name__ == "__main__":
    sys.exit(report("books/frankenstein.txt"))
