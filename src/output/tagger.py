# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from os import path

from nltk import PorterStemmer
from classifiers import KFFClassifier


# Tags the text
class Tagger:

    # Constructor for the Tagger
    def __init__(self, _type):
        self.classifier = None

        if _type == "kff":
            self.classifier = KFFClassifier(path.join('data', 'kff_stemmed.csv'))

    # Tag the text
    def tag(self, text):

        if self.classifier is None:
            return ""

        result = ""
        words = text.split()
        for word in words:

            if self.classifier.is_difficult(word):
                result += "<a href='#'>" + word + "</a>" + " "
            else:
                result += word + " "

        return result