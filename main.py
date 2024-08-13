import sys
from typing import Mapping, Sequence


def main() -> int:
    book = "books/frankenstein.txt"
    text = load_book(book)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(get_report(book, word_count, character_count))
    return 0

def get_report(book: str, word_count: int, character_count: Mapping[str, int]) -> str:
    report = f"--- Begin report of {book} ---\n"

    report += f"{word_count} word{"s" if word_count != 1 else ""} found in the document\n\n\n"

    sorted_characters = sort_character_count(character_count)
    
    for ch, count in sorted_characters:
        report += f"The '{ch}' character was found {count} time{"s" if count != 1 else ""}\n"

    report += "--- End report ---"
    
    return report

def load_book(path: str) -> str:
    with open(path) as f:
        return f.read()


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> Mapping[str, int]:
    count: dict[str, int] = {}

    for ch in text:
        lowered = ch.lower()

        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count

def sort_character_count(character_count: Mapping[str, int]) -> Sequence[tuple[str, int]]:
    return sorted(((ch, character_count[ch]) for ch in character_count if ch.isalpha()), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    sys.exit(main())
