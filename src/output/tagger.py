# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from os import path

from nltk import PorterStemmer
from classifiers import KFFClassifier
from classifiers import TFClassifier
from classifiers import DFClassifier
from classifiers import ITFIDFClassifier
from classifiers import SyllablesClassifier

# Tags the text
class Tagger:

    # Constructor for the Tagger
    def __init__(self, _type):
        self.classifier = None

        if _type == "kff":
            self.classifier = KFFClassifier(path.join('data', 'kff_stemmed.csv'))
        elif _type == "tf":
            self.classifier = TFClassifier(path.join('data', 'tf_stemmed.csv'))
        elif _type == "df":
            self.classifier = DFClassifier(path.join('data', 'df_stemmed.csv'))
        elif _type == "itfidf":
            self.classifier = ITFIDFClassifier(path.join('data', 'itfidf_stemmed.csv'))
        elif _type == "syllables":
            self.classifier = SyllablesClassifier(path.join('data', 'syllables_stemmed.csv'))

    # Tag the text
    def tag(self, text):

        if self.classifier is None:
            return ""

        result = ""
        words = text.split()
        for word in words:

            if self.classifier.is_difficult(word):
                result += "[" + word + "]" + " "
            else:
                result += word + " "

        return result