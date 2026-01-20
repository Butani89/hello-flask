from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello and Goodbye! NEW Testing 2222222'


if __name__ == '__main__':
    app.run(debug=True)