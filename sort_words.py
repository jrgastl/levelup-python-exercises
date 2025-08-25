'''
Author Notes:
I started this challenge right after checking the instructor solution for the challenge 2 (is_palindrome2.py), so the use of regular expressions was more or less automatic.
The instructor solution was more elegant in the end by using join() method to put everything together in one line.
'''

import re

def sort_words(phrase):
    words = re.findall(r'[A-z]+', phrase)
    words.sort(key=str.casefold)
    final_string = " ".join(words)
    print(final_string)

# Please, uncomment the line below to execute the code with the example given
# sort_words('Text phrase animals Fruits Vegetables')