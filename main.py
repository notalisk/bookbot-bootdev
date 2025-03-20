from stats import count_words
from stats import count_chars
from stats import sort_chars
from stats import print_chars
import sys

def get_book_text(path):
    with open(path) as book:
        return book.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        print(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    count_words(get_book_text(path))
    print("--------- Character Count -------")
    sorted = sort_chars(count_chars(get_book_text(path)))
    print_chars(sorted)
    print("============= END ===============")

main()