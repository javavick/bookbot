import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_filepath():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    return sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def report(filepath, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----------")
    for char in char_count:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

    
def main():
    filepath = get_filepath()
    book_text = get_book_text(filepath)
    char_count = get_char_count(book_text)

    report(filepath, get_word_count(book_text), sort_char_count(char_count))

main()
