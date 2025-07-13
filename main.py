import sys
from stats import (
    get_word_count,
    get_char_count,
    sort_char_count
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = (sys.argv[1])
    text = get_book_text(book_path)
    length = get_word_count(text)
    char_dict = get_char_count(text)
    sorted_char_list = sort_char_count(char_dict)
    print_report(book_path, length, sorted_char_list)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def print_report(book_path, length, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        if not i["char"].isalpha(): 
            continue
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")


main()
