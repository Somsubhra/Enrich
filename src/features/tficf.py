# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from os import walk, path, stat

from extras import Logger


# The term frequency inverse chapter frequency class
class TFICF:

    # Constructor for the TFICF class
    def __init__(self, in_dir, out_file):
        self.in_dir = in_dir
        self.out_file = out_file

    # Run the TFICF
    def run(self):
        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        Logger.log_message('Running TFICF')

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                # Calculate TFICF

        Logger.log_success('Finished TFICF')

        Logger.log_message('Writing results to ' + self.out_file)
        self.dump_results()
        Logger.log_success('Finished writing results to ' + self.out_file)

    def dump_results(self):
        pass