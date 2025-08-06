from stats import get_num_words, get_num_characters, get_book_report
import sys 


def get_book_text(file_path) -> str:
    with open(file_path) as data:
        book = data.read()
    return book


def main(): 
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)

    get_book_report(book)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

main()