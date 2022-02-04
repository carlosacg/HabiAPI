from flask import Flask
app = Flask(__name__)
from controlador import *


if __name__ == '__main__':
    app.run('0.0.0.0', 8084, debug=True)
