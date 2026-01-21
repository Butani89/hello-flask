from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'JIRA IS NICE denna gången är det rätt'


if __name__ == '__main__':
    app.run(debug=True)