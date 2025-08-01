import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_character_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        word_count = get_word_count(filepath)
        character_count = get_character_count(filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dictionary in character_count:
            print(f"{dictionary['char']}: {dictionary['num']}")
        print("============= END ===============")
main()
