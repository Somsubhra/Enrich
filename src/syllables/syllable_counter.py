# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# The syllable counter class
class SyllableCounter:

    # Constructor for the syllable counter class
    def __init__(self, in_dir, out_file, dict_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.dict_file = dict_file
        self.syllable_val = {}

    # Run the syllable counter
    def run(self):

        # Build up the syllable count dictionary
        dictionary = open(self.dict_file, 'r')

        for line in dictionary.readlines():
            cols = line.split(';')
            self.syllable_val[cols[2]] = cols[0]

        dictionary.close()