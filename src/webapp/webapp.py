# Headers
__author__ = 'Somsubhra Bairi'
__email__ = 'somsubhra.bairi@gmail.com'


# All imports
from flask import Flask


# The Web App class
class WebApp:

    # Constructor for the Web App class
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug

        self.app = Flask(__name__)

        # Index route
        @self.app.route("/")
        def index():
            return "Enrich"

    # Run the Web App
    def run(self):
        self.app.run(self.host, self.port, self.debug)