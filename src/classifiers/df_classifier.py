# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from extras import Logger

from nltk import PorterStemmer


# Classify according to document frequency
class DFClassifier:

    # Constructor for the DFClassifier
    def __init__(self, dict_file):
        dictionary_file = open(dict_file)

        self.document_frequencies = {}

        self.avg_df = 0

        # Construct the document frequency dictionary
        for line in dictionary_file.readlines():
            cols = line.split(";")
            self.document_frequencies[cols[0]] = int(cols[1])
            self.avg_df += int(cols[1])

        self.avg_df /= len(self.document_frequencies)

        dictionary_file.close()

    # Classify the word
    def is_difficult(self, word):
        if word.isdigit():
            return False

        sanitized_word = ''.join(e for e in word if e.isalnum()).lower()
        stemmed_word = PorterStemmer().stem_word(sanitized_word)

        if stemmed_word in self.document_frequencies:
            return self.document_frequencies[stemmed_word] < self.avg_df * 1
        else:
            return True