from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project/new')
def create():
    return 'Hello!'


@app.route('/project/{id}')
def detail():
    return 'Hello!'


@app.route('/project/{id}/edit')
def edit():
    return 'Hello!'


@app.route('/project/{id}/delete')
def delete():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
