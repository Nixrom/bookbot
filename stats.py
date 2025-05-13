check_characters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "]", "[", "|", "}", "{", "‘", "'", ";", ":", "/", ".", ",", "?", ">", "<", "”", " ", "\", """)

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def word_split(book):
    text = get_book_text(book)
    words = text.split()
    return words

def word_count(book):
    words = word_split(book)
    word_num = 0
    for word in words:
        word_num += 1
    return word_num

def main(book_text):
    print(book_text)

def letter_count(text):
    book = get_book_text(text)
    full_letter_count = {}
    temp_letter_count = {}
    lower_text = book.lower()
    for letter in check_characters:
        letter_count_check = lower_text.count(letter)
        if letter_count_check > 0:
            temp_letter_count.update({letter : letter_count_check})
    full_letter_count = dict(reversed(sorted(temp_letter_count.items(), key=lambda item: item[1])))
    return full_letter_count
    

get_num_words = (f"Found {word_count("./books/frankenstein.txt")} total words")
book_letter_count = letter_count("./books/frankenstein.txt")