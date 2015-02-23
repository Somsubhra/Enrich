# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from extras import Logger

from nltk import PorterStemmer


# Classify according to document frequency
class ITFIDFClassifier:

    # Constructor for the ITFIDFClassifier
    def __init__(self, dict_file):
        dictionary_file = open(dict_file)

        self.itfidf_dictionary = {}

        self.avg_itfidf = 0

        # Construct the document frequency dictionary
        for line in dictionary_file.readlines():
            cols = line.split(";")
            self.itfidf_dictionary[cols[0]] = int(cols[1])
            self.avg_itfidf += int(cols[1])

        self.avg_itfidf /= len(self.itfidf_dictionary)

        dictionary_file.close()

    # Classify the word
    def is_difficult(self, word):
        if word.isdigit():
            return False

        sanitized_word = ''.join(e for e in word if e.isalnum()).lower()
        stemmed_word = PorterStemmer().stem_word(sanitized_word)

        if stemmed_word in self.itfidf_dictionary:
            return self.itfidf_dictionary[stemmed_word] > self.avg_itfidf / 16
        else:
            return True