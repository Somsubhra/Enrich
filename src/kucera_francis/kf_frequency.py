# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# The Kucera Francis frequency class
class KFFrequency:

    # Constructor for the Kucera Francis frequency class
    def __init__(self, in_dir, out_file, dict_file):
        self.in_dir = in_dir
        self.out_file = out_file
        self.dict_file = dict_file
        self.kf_val = {}

    # Run the Kucera Francis frequency calculator
    def run(self):

        # Build up the Kucera Francis dictionary
        dictionary = open(self.dict_file, 'r')

        for line in dictionary.readlines():
            cols = line.split(';')
            self.kf_val[cols[2]] = cols[1]

        dictionary.close()