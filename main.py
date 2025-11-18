from stats import get_num_words
from stats import character_counter
from stats import sorted_list
import sys

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) == 2:
        num_words = get_num_words(get_book_text(sys.argv[1]))
        counted_dictionary = character_counter(get_book_text(sys.argv[1]))

        sorted = sorted_list(counted_dictionary)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for element in sorted:
            if element["char"].isalpha():
                print (f"{element["char"]}: {element["num"]}")
            else:
                continue

        print("============= END ===============")
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

main()


