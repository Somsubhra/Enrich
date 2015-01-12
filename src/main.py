# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from webapp import WebApp
from txtdump import TxtDump
from logger import Logger

import sys

# Constant declarations
DEBUG = True


# The main function
def main():

    args = sys.argv

    if len(args) < 2:
        Logger.log_usage('\n./run runserver\n./run txtdump')
        return

    if args[1] == 'runserver':
        web_app = WebApp('127.0.0.1', 5000, DEBUG)
        web_app.run()
        return

    elif args[1] == 'txtdump':
        txt_dump = TxtDump('corpus', 'tmp')
        txt_dump.dump()
        return

    else:
        Logger.log_usage('\n./run runserver\n./run txtdump')
        return


# Run the main function
if __name__ == '__main__':
    main()