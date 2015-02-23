# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'

# All imports
from extras import Logger


# Calculates the Inverse Term Frequency - Inverse Document Frequency
class ITFIDF:

    # Constructor for the ITFIDF
    def __init__(self, out_file, tf_dict, df_dict):
        self.out_file = out_file
        self.tf_dict = tf_dict
        self.df_dict = df_dict

        self.tf_dictionary = {}
        self.df_dictionary = {}

        self.itfidf = {}

    # Run the ITFIDF
    def run(self):

        Logger.log_message("Running ITFIDF")

        Logger.log_message("Reading " + self.tf_dict)
        tf_dict_file = open(self.tf_dict)

        for line in tf_dict_file.readlines():
            cols = line.split(";")
            self.tf_dictionary[cols[0]] = int(cols[1])

        tf_dict_file.close()

        Logger.log_message("Reading " + self.df_dict)
        df_dict_file = open(self.df_dict)

        for line in df_dict_file.readlines():
            cols = line.split(";")
            self.df_dictionary[cols[0]] = int(cols[1])

        max_tf = max(self.tf_dictionary.values())
        max_df = max(self.df_dictionary.values())

        for word in self.df_dictionary:
            self.itfidf[word] = (max_tf * max_df) / (self.tf_dictionary[word] * self.df_dictionary[word])

        Logger.log_message("Writing results to " + self.out_file)
        self.dump_results()
        Logger.log_success("Finished writing results to " + self.out_file)

    # Dump the results to the output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        for word in self.itfidf:
            output_file.write(word + ";" + str(self.itfidf[word]) + "\n")

        output_file.close()