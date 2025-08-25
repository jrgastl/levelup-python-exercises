'''
Author Notes:
The module collections could have been used in this challenge as well, like the instructor solution. I also realized that I need to improve how to name strings so the code
is clearer. Finally, I had to change the code after discovering that modifying the file strings to uppercase before applying the pattern doesn't lead to the correct results,
returning a smaller number of words.

Briefing:
Input: path to a text file
Output: print message with:
    - total number of words
    - top 20 most frequent words
    - top 20 words ocurrence

Example:
>>> count_words('input.txt')

    Total Words: 473

    Top 20 Words:
    TEXT        13
    CHALLENGE   11
    WORDS       9
    YOUR        5
    FUNCTION    5

Words contain:
    -Letters
    -Numbers
    -Apostrophes
    -Hyphens
'''
import re

def count_words(file_path):
    with  open(file_path, 'r', encoding='UTF-8') as file:
        all_words = re.findall(r"[A-Za-z0-9-']+", file.read())
        all_words = [word.upper() for word in all_words]
    words_ocurrence = {}
    for word in all_words:
        words_ocurrence[word] = words_ocurrence.get(word,0) + 1
    ocurrencesList = sorted(list(words_ocurrence.values()),reverse=True)
    top20 = [(word,ocurrence) for ocurrence in ocurrencesList[0:20] for word in words_ocurrence if words_ocurrence[word] == ocurrence]
    print(f'\nTotal Words: {len(all_words)}\n\nTop 20 Words:\n')
    for place in top20:
        print(f'{place[0]}\t{place[1]}')

# Please, uncomment the line below to execute the code with the example given
# count_words('./texts/pg100.txt')