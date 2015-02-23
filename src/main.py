# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
import sys
from os import path

from webapp import WebApp
from corpus import TxtDump
from corpus import Sanitizer
from corpus import Stemmer
from features import TermFrequency
from features import DocumentFrequency
from features import ITFIDF
from features import KFFrequency
from features import SyllableCounter
from extras import Logger
from extras import PsycholinguisticDbCreator


# Constant declarations
DEBUG = True


# The main function
def main():

    args = sys.argv

    usage = '''
            ./run txtdump\t<Gives the text dump of corpus>
            ./run sanitize\t<Sanitize the text dump to remove white spaces, etc.>
            ./run stem\t\t<Stem the sanitized text>
            ./run tf\t\t<Calculate the raw term frequency>
            ./run df\t\t<Calculate the document frequency>
            ./run itfidf\t<Calculate the inverse term frequency - inverse document frequency>
            ./run dict\t\t<Create the psycholinguistic dictionary>
            ./run kff\t\t<Calculate the Kucera Francis frequency>
            ./run syl\t\t<Calculate the number of syllables>
            ./run server\t<Run the application server>
            '''

    if len(args) < 2:

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

    elif args[1] == 'df':
        df = DocumentFrequency(path.join('tmp', 'stemmed'), path.join('data', 'df_stemmed.csv'),
                               path.join('data', 'tf_stemmed.csv'))
        df.run()
        return

    elif args[1] == 'itfidf':
        itfidf = ITFIDF(path.join('data', 'itfidf_stemmed.csv'),
                        path.join('data', 'tf_stemmed.csv'),
                        path.join('data', 'df_stemmed.csv'))
        itfidf.run()
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
        return

    elif args[1] == 'syl':
        syllable_counter = SyllableCounter(path.join('tmp', 'stemmed'),
                                           path.join('data', 'syllables_stemmed.csv'),
                                           path.join('data', 'psycholinguistic_db.csv'))
        syllable_counter.run()
        return

    else:
        Logger.log_usage(usage)
        return


# Run the main function
if __name__ == '__main__':
    main()