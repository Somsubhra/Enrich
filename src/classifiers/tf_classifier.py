# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from extras import Logger

from nltk import PorterStemmer


# Classify according to raw term frequency
class TFClassifier:

    # Constructor for the TFClassifier
    def __init__(self, dict_file):
        dictionary_file = open(dict_file)

        self.term_frequencies = {}

        self.avg_tf = 0

        # Construct the term frequency dictionary
        for line in dictionary_file.readlines():
            cols = line.split(";")
            self.term_frequencies[cols[0]] = int(cols[1])
            self.avg_tf += int(cols[1])

        self.avg_tf /= len(self.term_frequencies)

        dictionary_file.close()

    # Classify the word
    def is_difficult(self, word):
        if word.isdigit():
            return False

        sanitized_word = ''.join(e for e in word if e.isalnum()).lower()
        stemmed_word = PorterStemmer().stem_word(sanitized_word)

        if stemmed_word in self.term_frequencies:
            return self.term_frequencies[stemmed_word] < self.avg_tf / 8
        else:
            return True