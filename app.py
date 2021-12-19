from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project/new', methods=['GET', 'POST'])
def create():
    print(request.form)
    return render_template('projectform.html')


@app.route('/project/{id}')
def detail():
    return render_template('detail.html')


@app.route('/project/{id}/edit')
def edit():
    pass


@app.route('/project/{id}/delete')
def delete():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
