import sys
from stats import (
    get_book_text,
    get_word_count,
    get_character_count,
    sort_character_library)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        word_count = get_word_count(filepath)
        character_count = get_character_count(filepath)
        character_library = sort_character_library (filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dictionary in character_library:
            print(f"{dictionary['char']}: {dictionary['num']}")
        print("============= END ===============")
main()
