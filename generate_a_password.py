"""
Author Notes:
I was really happy with this code and the optimizations that were done. In the end I learned that the random module is not suitable for security purposes,
but I understand the exercise was valid anyway.

Briefing:
Create a password generator that takes as input the number of words 
the password should have and generate a string of random words of 
the Diceware list separated by spaces as password.
>>> generate_passphrase(5):

    'vice fame tango abide verb' 
"""
import random
import re

def roll_dices():
    keyword = ''.join(str(random.randint(1, 6)) for _ in range(0,5))
    return keyword
          
def generate_passphrases(length):
    with open('./texts/diceware.wordlist.asc' ,'r', encoding='utf-8') as diceware_file:
        diceware_words= [line.split() for line in diceware_file.readlines() if re.match(r'^[1-6]{5}\s', line)]
    diceware_dict = {words[0]:words[1] for words in diceware_words}
    
    passphrase = ' '.join(diceware_dict[roll_dices()] for _ in range(length))
    print(passphrase)

# Please, uncomment the line below to execute the code with the example given            
# generate_passphrases(5)