# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# Logger class
class Logger:

    # Log error
    @staticmethod
    def log_error(msg):
        print '\033[91m' + 'Error: ' + msg + '\033[0m'

    # Log success
    @staticmethod
    def log_success(msg):
        print '\033[92m' + 'Success: ' + msg + '\033[0m'

    # Log message
    @staticmethod
    def log_message(msg):
        print '\033[94m' + '--' + msg + '\033[0m'

    # Log usage
    @staticmethod
    def log_usage(msg):
        print '\033[93m' + 'Usage: ' + msg + '\033[0m'