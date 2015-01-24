#!/usr/bin/env python

# Creates a CSV of psycholinguistic dictionary
# downloaded from web

# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from logger import Logger


# The psycholinguistic database creator
class PsycholinguisticDbCreator:

    # Constructor for the database creator
    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file

    # Create the database
    def create(self):
        Logger.log_message('Creating psycholinguistic dictionary database')

        input_file = open(self.in_file, 'r')
        output_file = open(self.out_file, 'w')

        for line in input_file.readlines():
            output_file.write(';'.join(word.lower() for word in line.split()) + '\n')

        input_file.close()
        output_file.close()

        Logger.log_success('Created psycholinguistic dictionary database')