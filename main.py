from stats import get_num_words
from stats import character_counter
from stats import sorted_list

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    counted_dictionary = character_counter(get_book_text("books/frankenstein.txt"))

    sorted = sorted_list(counted_dictionary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for element in sorted:
        if element["char"].isalpha():
            print (f"{element["char"]}: {element["num"]}")
        else:
            continue

    print("============= END ===============")

main()


