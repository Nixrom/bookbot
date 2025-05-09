def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def word_split(book_text):
    words = book_text.split()
    return words

def word_count(words):
    word_num = 0
    for word in words:
        word_num += 1
    return word_num

def main(book_text):
    print(book_text)

print(f"{word_count(word_split(get_book_text("./books/frankenstein.txt")))} words found in the document")

