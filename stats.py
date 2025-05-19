import sys
check_characters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "-", "=", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "]", "[", "|", "}", "{", "‘", "'", ";", ":", "/", ".", ",", "?", ">", "<", "”", " ", "\", """)
if len(sys.argv) == 2:
    text_variable = sys.argv[1:2]
    text = text_variable.pop()
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

    def sort_on(dict):
        return dict["num"]

    def letter_count(text):
        book = get_book_text(text)
        sorted_letter_count = []
        temp_letter_count = []
        output_letter_count = []
        lower_text = book.lower()
        for letter in check_characters:
            letter_count_check = lower_text.count(letter)
            if letter_count_check > 0:
                temp_letter_count.append({"char": letter, "num": letter_count_check})
        sorted_letter_count = sorted(temp_letter_count, reverse=True, key=sort_on)
        for dictionary in sorted_letter_count:
            output_letter_count.append(f"{dictionary["char"]}" + ": " + f"{dictionary["num"]}")


        return output_letter_count
    

    get_num_words = (f"Found {word_count(text)} total words")
    book_letter_count = letter_count(text)
else:
    get_num_words = ("")
    book_letter_count = ("")