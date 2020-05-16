from flask import Flask
from flask import Flaskapp = Flask(__name__)
@app.route('/')
def Hello_World():
    return 'Hello Africa'

if __name__ == '__main__':
    app.run()