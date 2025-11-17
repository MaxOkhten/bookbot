def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    num_words = len(get_book_text("books/frankenstein.txt").split())

    print(f"Found {num_words} total words")

main()