# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from os import walk, path, stat, mkdir, makedirs
from subprocess import call


# The text dumping class
class TxtDump:

    # Constructor for the text dumping class
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Dump the text
    def dump(self):
        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            return

        # Create the output directory
        try:
            stat(self.out_dir)
        except:
            mkdir(self.out_dir)

        # Walk through the input directory
        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                out_file = path.join(self.out_dir, dir_path, file_name + ".txt")
                output_dir = path.join(self.out_dir, dir_path)

                # Create the output directory path
                try:
                    stat(output_dir)
                except:
                    makedirs(output_dir)

                TxtDump.extract_text(in_file, out_file)

    # Extract the text
    @staticmethod
    def extract_text(in_file, out_file):
        call(['pdftotext', in_file, out_file])