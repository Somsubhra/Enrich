# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from os import walk, path, stat, makedirs
from subprocess import call

from extras import Logger


# The text dumping class
class TxtDump:

    # Constructor for the text dumping class
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Dump the text
    def run(self):

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Corpus not found')
            return

        # Create the output directory
        try:
            stat(self.out_dir)
        except:
            makedirs(self.out_dir)

        Logger.log_message('Started text dumping')

        # Walk through the input directory
        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                out_file = path.join(self.out_dir, file_name + '_' + dir_path.replace('/', '_') + '.txt')

                TxtDump.extract_text(in_file, out_file)

        Logger.log_success('Finished dumping text')

    # Extract the text
    @staticmethod
    def extract_text(in_file, out_file):
        Logger.log_message('Dumping ' + in_file)
        call(['pdftotext', in_file, out_file])