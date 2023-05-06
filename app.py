from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db =SQLAlchemy(app)
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)



@app.route('/')
def index():
    todo_list = Task.query.all()
    total_tasks = Task.query.count()
    return render_template('dashboard/home.html', todo_list = todo_list ,  total_tasks=total_tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     title = request.form.get('title')
#     new_task = Task(title=title)
#     db.session.add(new_task)
#     db.session.commit 
#     return title

@app.route('/test')
def test():
    return 'test'

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>')
def update(id):
    task = Task.query.filter_by(id=id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/home')
def home():
    todo_list = Task.query.all()
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(complete=True).count()
    pending_tasks = total_tasks - completed_tasks
    return render_template('dashboard/home.html', todo_list=todo_list, total_tasks=total_tasks, completed_tasks=completed_tasks, pending_tasks=pending_tasks )
    
@app.route('/about')
def about():
    return render_template('dashboard/about.html')

if __name__== '__main__':
    app.run(debug=True)

    


