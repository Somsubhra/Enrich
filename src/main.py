# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from webapp import WebApp
from txtdump import TxtDump

import sys

# Constant declarations
DEBUG = True


# The main function
def main():

    args = sys.argv

    if len(args) < 2:
        return

    if args[1] == 'runserver':
        web_app = WebApp('127.0.0.1', 5000, DEBUG)
        web_app.run()

    elif args[1] == 'txtdump':
        txt_dump = TxtDump('corpus', 'tmp')
        txt_dump.dump()

    else:
        txt_dump = TxtDump('corpus', 'tmp')
        txt_dump.dump()

        web_app = WebApp('127.0.0.1', 5000, DEBUG)
        web_app.run()
        
        return


# Run the main function
if __name__ == '__main__':
    main()