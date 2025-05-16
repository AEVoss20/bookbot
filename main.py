def words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def main():
    from stats import get_book_text
    book = get_book_text("books/frankenstein.txt")
    count = words(book)
    print(f"{count} words found in the document")

main()