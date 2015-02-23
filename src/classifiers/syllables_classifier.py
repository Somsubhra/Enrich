# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from extras import Logger

from nltk import PorterStemmer


# Classify according to number of syllables
class SyllablesClassifier:

    # Constructor for the SyllablesClassifier
    def __init__(self, dict_file):
        dictionary_file = open(dict_file)

        self.syllables = {}

        self.avg_syl = 0

        # Construct the syllables dictionary
        for line in dictionary_file.readlines():
            cols = line.split(";")
            self.syllables[cols[0]] = int(cols[1])
            self.avg_syl += int(cols[1])

        self.avg_syl /= len(self.syllables)

        dictionary_file.close()

    # Classify the word
    def is_difficult(self, word):
        if word.isdigit():
            return False

        sanitized_word = ''.join(e for e in word if e.isalnum()).lower()
        stemmed_word = PorterStemmer().stem_word(sanitized_word)

        if stemmed_word in self.syllables:
            return self.syllables[stemmed_word] > 2
        else:
            return True