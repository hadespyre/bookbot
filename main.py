from stats import get_num_words
from stats import get_char_count
from stats import print_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    print_report(contents, file_path)
    

main()