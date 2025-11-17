from stats import get_num_words
from stats import character_counter

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))

    print(f"Found {num_words} total words")

    print(character_counter(get_book_text("books/frankenstein.txt")))

main()


