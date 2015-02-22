# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from os import walk, path, stat

from extras import Logger


# The syllable counter class
class SyllableCounter:

    # Constructor for the syllable counter class
    def __init__(self, in_dir, out_file, dict_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.dict_file = dict_file
        self.syllable_val = {}
        self.syllable_res = {}

    # Run the syllable counter
    def run(self):

        # Build up the syllable count dictionary
        dictionary = open(self.dict_file, 'r')

        Logger.log_message("Reading " + self.dict_file)

        for line in dictionary.readlines():
            cols = line.split(';')
            self.syllable_val[cols[0]] = int(cols[2])

        dictionary.close()

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        Logger.log_message('Running syllable counter')

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)
                self.count_syllables(in_file)

        Logger.log_success('Finished syllable counting')

        Logger.log_message('Writing results to ' + self.out_file)
        self.dump_results()
        Logger.log_success('Finished writing results to ' + self.out_file)

    # Count the Syllables for words in file
    def count_syllables(self, in_file):
        Logger.log_message('Counting number of syllables for ' + in_file)

        input_file = open(in_file, 'r')

        for line in input_file.readlines():
            for word in line.split():

                if word.isdigit():
                    continue

                if word in self.syllable_val:
                    # If word is present in psycholinguistic dictionary
                    self.syllable_res[word] = self.syllable_val[word]
                else:
                    self.syllable_res[word] = 0

    # Dump the results to output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        for word in self.syllable_res:
            output_file.write(word + ";" + str(self.syllable_res[word]) + "\n")

        output_file.close()