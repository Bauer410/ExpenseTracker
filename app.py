from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Our Software Methods and Tools project'


if __name__ == '__main__':
    app.run()
