# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from extras import Logger
from nltk import PorterStemmer


# Classifier based on Kucera Francis frequency
class KFFClassifier:

    # Constructor for the KFF classifier
    def __init__(self, dict_file):
        dictionary_file = open(dict_file)

        self.kf_frequencies = {}

        # Construct the KF Frequency dictionary
        for line in dictionary_file.readlines():
            cols = line.split(";")
            self.kf_frequencies[cols[0]] = int(cols[1])

        dictionary_file.close()

    # Classify the word
    def is_difficult(self, word):
        if word.isdigit():
            return False

        sanitized_word = ''.join(e for e in word if e.isalnum()).lower()
        stemmed_word = PorterStemmer().stem_word(sanitized_word)

        if stemmed_word in self.kf_frequencies:
            return self.kf_frequencies[stemmed_word] == 0
        else:
            return True