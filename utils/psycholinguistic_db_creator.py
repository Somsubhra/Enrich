#!/usr/bin/env python

# Creates a CSV of psycholinguistic dictionary
# downloaded from web

# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
import sys


def main():

    if len(sys.argv) < 3:
        usage = '''
            ./psycholiguistic_db_creator.py <input_file> <output_file>
        '''
        message = '\033[93m' + 'Usage: ' + usage + '\033[0m'
        print(message)
        return

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    input_file = open(in_file, 'r')
    output_file = open(out_file, 'w')

    for line in input_file.readlines():
        output_file.write(';'.join(word.lower() for word in line.split()) + '\n')

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()