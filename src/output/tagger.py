# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from nltk import PorterStemmer


# Tags the text
class Tagger:

    # Constructor for the Tagger
    def __init__(self):
        pass

    # Tag the text
    @staticmethod
    def tag(text):
        result = ""
        words = text.split()
        for word in words:

            # Strip the special characters
            sanitized_word = ''.join(e for e in word if e.isalnum())

            # Stem the word
            stemmed_word = PorterStemmer().stem_word(sanitized_word)

            result += stemmed_word + " "

        return result