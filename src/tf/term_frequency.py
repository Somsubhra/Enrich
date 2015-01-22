# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from logger import Logger

from os import walk, path, stat
import sqlite3


# The term frequency counter class
class TermFrequency:

    # Constructor for the term frequency counter class
    def __init__(self, in_dir, out_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.frequencies = {}

    # Run the term frequency counter
    def run(self):

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        Logger.log_message('Running term frequency counter')

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                self.count_term_frequency(in_file)

        Logger.log_success('Finished term frequency counting')

        Logger.log_message('Writing results to ' + self.out_file)
        self.dump_results()
        Logger.log_success('Finished writing results to ' + self.out_file)

    # Count the term frequency for a file
    def count_term_frequency(self, in_file):

        Logger.log_message('Counting term frequency for ' + in_file)

        input_file = open(in_file, 'r')

        for line in input_file.readlines():
            for word in line.split():
                if self.frequencies.has_key(word):
                    self.frequencies[word] += 1
                else:
                    self.frequencies[word] = 1

        input_file.close()

    # Dump the results
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        for term in self.frequencies:
            output_file.write(term + ";" + str(self.frequencies[term]) + "\n")

        output_file.close()