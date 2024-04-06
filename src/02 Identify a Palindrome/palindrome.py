from string import punctuation


def is_palindrome(phrase: str):
    phrase = phrase.lower().translate({ord(i): None for i in punctuation + ' '})
    return phrase[:] == phrase[::-1]

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
