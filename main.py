from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_loc = sys.argv[1] #location of the book
    f = open(book_loc, "r")
    words = f.read()                
    #Get the list of characters:
    char_list = get_sorted_chars(get_character_count(words))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(words)} total words")
    print("--------- Character Count -------") 
    for dic in char_list:
        for val,cal in dic.items():
            print(f'{val}: {cal}')
    print("============= END ===============")
if __name__ == "__main__":
    main()
