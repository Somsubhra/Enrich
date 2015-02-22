#!/usr/bin/env python

# Creates a CSV of psycholinguistic dictionary
# downloaded from web

# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from nltk import PorterStemmer

from extras import Logger


# The psycholinguistic database creator
class PsycholinguisticDbCreator:

    # Constructor for the database creator
    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file
        self.kf_frequencies = {}
        self.syllables = {}

    # Create the database
    def create(self):
        Logger.log_message('Creating psycholinguistic dictionary database')

        input_file = open(self.in_file, 'r')
        output_file = open(self.out_file, 'w')

        for line in input_file.readlines():
            items = line.split()
            word = PorterStemmer().stem_word(items[2].lower())
            kff = items[1]
            syl = items[0]

            if word in self.kf_frequencies:
                # Select the stemmed word with the maximum KF Frequency
                if kff > self.kf_frequencies[word]:
                    self.kf_frequencies[word] = kff
            else:
                self.kf_frequencies[word] = kff

            if word in self.syllables:
                # Select the stemmed word with minimum number of syllables
                if syl < self.syllables[word]:
                    self.syllables[word] = syl
            else:
                self.syllables[word] = syl

        # Dump the contents to the output file
        for word in self.kf_frequencies:
            output_file.write(word + ";" + self.kf_frequencies[word] + ";" + self.syllables[word] + "\n")

        input_file.close()
        output_file.close()

        Logger.log_success('Created psycholinguistic dictionary database')