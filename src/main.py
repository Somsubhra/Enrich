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
from psycholinguistic_db import PsycholinguisticDbCreator
from kucera_francis import KFFrequency

import sys
from os import path

# Constant declarations
DEBUG = True


# The main function
def main():

    args = sys.argv

    if len(args) < 2:
        usage = '''
        ./run txtdump\t<Gives the text dump of corpus>
        ./run sanitize\t<Sanitize the text dump to remove white spaces, etc.>
        ./run stem\t<Stem the sanitized text>
        ./run tf\t<Calculate the raw term frequency>
        ./run tficf\t<Calculate the term frequency - inverse chapter frequency>
        ./run dict\t<Create the psycholinguistic dictionary>
        ./run kff\t<Calculate the Kucera Francis frequency>
        ./run server\t<Run the application server>
        '''
        Logger.log_usage(usage)
        return

    if args[1] == 'server':
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
        return

    elif args[1] == 'dict':
        dict_creator = PsycholinguisticDbCreator(path.join('data', 'psycholinguistic_db'),
                                                 path.join('data', 'psycholinguistic_db.csv'))
        dict_creator.create()
        return

    elif args[1] == 'kff':
        kf_freq_counter = KFFrequency(path.join('tmp', 'stemmed'),
                                      path.join('data', 'kff_stemmed.csv'),
                                      path.join('data', 'psycholinguistic_db.csv'))
        kf_freq_counter.run()

    else:
        Logger.log_usage('\n./run runserver\n./run txtdump')
        return


# Run the main function
if __name__ == '__main__':
    main()