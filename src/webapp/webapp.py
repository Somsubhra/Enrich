# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from logger import Logger

from flask import Flask, render_template, request


# The Web App class
class WebApp:

    # Constructor for the Web App class
    def __init__(self, host, port, debug):

        self.host = host
        self.port = port
        self.debug = debug

        self.app = Flask(__name__)

        # Index route
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/api/tag', methods=['GET', 'POST'])
        def api():
            if request.method == 'POST':
                return '[]'
            else:
                return 'POST /api/tag'

        Logger.log_success('Server started successfully')

    # Run the Web App
    def run(self):
        self.app.run(self.host, self.port, self.debug)