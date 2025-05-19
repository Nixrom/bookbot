from stats import book_letter_count
from stats import get_num_words 
import sys
if len(sys.argv) == 2: 
    book_path_variable = sys.argv[1:]
    book_path = book_path_variable.pop()
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    {get_num_words}
    --------- Character Count -------
    {book_letter_count}
    """)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

