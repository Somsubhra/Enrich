# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from re import split
from os import walk, path, stat, makedirs

from extras import Logger


# The text sanitizer class
class Sanitizer:

    # Constructor for the sanitizer
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Run the sanitizing process
    def run(self):

        # Check for the input directory
        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        # Create the output directory
        try:
            stat(self.out_dir)
        except:
            makedirs(self.out_dir)

        Logger.log_message('Started text sanitizing')

        # Walk through the input directory
        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:

                in_file = path.join(dir_path, file_name)
                out_file = path.join(self.out_dir, file_name + '_' + dir_path.replace('/', '_') + '.txt')

                Sanitizer.sanitize(in_file, out_file)

        Logger.log_success('Finished sanitizing text')


    # Sanitize the file
    @staticmethod
    def sanitize(in_file, out_file):

        Logger.log_message('Sanitizing ' + in_file)

        input_file = open(in_file, 'r')
        output_file = open(out_file, 'w')

        for input_line in input_file.readlines():
            output_line = ' '.join([word.lower() for word in split('\W', input_line) if word])
            output_file.write(output_line + '\n')

        input_file.close()
        output_file.close()