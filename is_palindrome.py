'''
Author Notes:
That was a great challenge to manipulate strings and slice lists. The implemenation is a bit rough, specially after learning about the regular expressions module.
'''
def is_palindrome(text):
    
    if type(text) != str:
        return False
    lower_text = text.lower()
    valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
    clean_text_list = []
    for letter in lower_text:
        if letter in valid_chars:
            clean_text_list.append(letter)
    return clean_text_list == clean_text_list[::-1]

# Please, uncomment the line below to execute the code with the example given
# print(is_palindrome("Go hang a salami - I'm a lasagna hog."))
