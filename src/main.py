# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from webapp import WebApp


# Constant declarations
DEBUG = True


# The main function
def main():
    webapp = WebApp("127.0.0.1", 5000, DEBUG)
    webapp.run()
    

# Run the main function
if __name__ == '__main__':
    main()