
from flask import Flask


dataBase = Flask(__name__)

@dataBase.route('/')
def hello():
    return "Hey, Flask you can creat all the material you want here chuy"

if __name__ == '__main__':
    dataBase.run(debug=True)
