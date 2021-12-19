from flask import render_template, url_for, request, redirect
from werkzeug.utils import redirect
from models import db, Project, app


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def create():
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'], desc=request.form['desc'], skills=request.form['skills'], github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


@app.route('/project/<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get(id)
    if request.form:
        project.title = request.form['title']
        project.date = request.form['date']
        project.desc = request.form['desc']
        project.skills = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editprojectform.html', project=project)


@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
