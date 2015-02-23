# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from os import walk, path, stat

from extras import Logger


# Counts the document frequency of a term
class DocumentFrequency:

    # Constructor for the document frequency
    def __init__(self, in_dir, out_file, dict_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.dict_file = dict_file

        self.document_frequencies = {}
        self.document_words = {}

    # Run the Document Frequency counter
    def run(self):

        dictionary = open(self.dict_file)

        Logger.log_message('Reading ' + self.dict_file)

        # Construct the dictionary
        for line in dictionary.readlines():
            items = line.split(";")
            self.document_frequencies[items[0]] = 0
            self.document_words[items[0]] = False

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        Logger.log_message('Running document frequency counter')

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)

                self.terms_in_document(in_file)

        Logger.log_message('Finished document frequency counting')

        Logger.log_message('Writing results to ' + self.out_file)
        self.dump_results()
        Logger.log_success('Finished writing results to ' + self.out_file)

    # Build the document frequencies
    def terms_in_document(self, in_file):

        Logger.log_message('Running document frequency counter for ' + in_file)

        input_file = open(in_file)

        # Reset words in document every time
        for word in self.document_words:
            self.document_words[word] = False

        # Set the words present in document to True
        for line in input_file.readlines():
            for word in line.split():
                self.document_words[word] = True

        for word in self.document_words:
            # If word present in document
            if self.document_words[word]:
                self.document_frequencies[word] += 1

    # Dump the results in the output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        for word in self.document_frequencies:
            output_file.write(word + ";" + str(self.document_frequencies[word]) + "\n")

        output_file.close()