import sys
from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
