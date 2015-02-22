# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from os import walk, path, stat

from extras import Logger


# The Kucera Francis frequency class
class KFFrequency:

    # Constructor for the Kucera Francis frequency class
    def __init__(self, in_dir, out_file, dict_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.dict_file = dict_file
        self.kf_val = {}
        self.kf_res = {}

    # Run the Kucera Francis frequency calculator
    def run(self):

        # Build up the Kucera Francis dictionary
        dictionary = open(self.dict_file, 'r')

        Logger.log_message("Reading " + self.dict_file)

        for line in dictionary.readlines():
            cols = line.split(';')
            self.kf_val[cols[0]] = int(cols[1])

        dictionary.close()

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        Logger.log_message('Running Kucera Francis frequency counter')

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                self.count_kf_frequency(in_file)

        Logger.log_success('Finished Kucera Francis frequency counting')

        Logger.log_message('Writing results to ' + self.out_file)
        self.dump_results()
        Logger.log_success('Finished writing results to ' + self.out_file)

    # Count Kucera Francis frequency for a file
    def count_kf_frequency(self, in_file):
        Logger.log_message('Counting Kucera Francis frequency for ' + in_file)

        input_file = open(in_file, 'r')

        for line in input_file.readlines():
            for word in line.split():
                if word in self.kf_val:
                    # If word is present in the psycholinguistic dictionary
                    self.kf_res[word] = self.kf_val[word]
                else:
                    self.kf_res[word] = 0

    # Dump the results to output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        for word in self.kf_res:
            output_file.write(word + ";" + str(self.kf_res[word]) + "\n")

        output_file.close()