from flask import Flask, render_template, request, redirect, url_for
from models import db, Todo  


app = Flask(__name__, template_folder="/app/templates", static_folder="/app/static")
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/mydatabase'
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form['todo']
    todo = Todo(task=task, done=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = Todo.query.get(id)
    if request.method == "POST":
        todo.task = request.form['todo']
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", todo=todo)

@app.route("/check/<int:id>", methods=["POST"])
def check(id):
    todo = Todo.query.get(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

