# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from webapp import WebApp
from txtdump import TxtDump
from logger import Logger
from sanitizer import Sanitizer
from stemmer import Stemmer
from tf import TermFrequency
from tficf import TFICF

import sys
from os import path

# Constant declarations
DEBUG = True


# The main function
def main():

    args = sys.argv

    if len(args) < 2:
        usage = '''
        ./run txtdump
        ./run sanitize
        ./run stem
        ./run tf
        ./run runserver
        '''
        Logger.log_usage(usage)
        return

    if args[1] == 'runserver':
        web_app = WebApp('127.0.0.1', 5000, DEBUG)
        web_app.run()
        return

    elif args[1] == 'txtdump':
        txt_dump = TxtDump('corpus', path.join('tmp', 'txtdump'))
        txt_dump.run()
        return

    elif args[1] == 'sanitize':
        sanitizer = Sanitizer(path.join('tmp', 'txtdump'), path.join('tmp', 'sanitized'))
        sanitizer.run()
        return

    elif args[1] == 'stem':
        stemmer = Stemmer(path.join('tmp', 'sanitized'), path.join('tmp', 'stemmed'))
        stemmer.run()
        return

    elif args[1] == 'tf':
        tf = TermFrequency(path.join('tmp', 'stemmed'), path.join('data', 'tf_stemmed.csv'))
        tf.run()
        tf = TermFrequency(path.join('tmp', 'sanitized'), path.join('data', 'tf_sanitized.csv'))
        tf.run()
        return

    elif args[1] == 'tficf':
        tficf = TFICF(path.join('tmp', 'stemmed'), path.join('data', 'tficf_stemmed.csv'))
        tficf.run()
        tficf = TFICF(path.join('tmp', 'sanitized'), path.join('data', 'tficf_sanitized.csv'))
        tficf.run()

    else:
        Logger.log_usage('\n./run runserver\n./run txtdump')
        return


# Run the main function
if __name__ == '__main__':
    main()