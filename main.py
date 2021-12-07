from flask import Flask
from flask import render_template

from flaskr.db import get_db

app = Flask(__name__)

from flaskr import db

db.init_app(app)

@app.route("/")
def hello_world():
    db = get_db()
    print("!!!!!", db)
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template('categories-list.html', categories=categories)


@app.route('/category/<category_name>')
def show_user_profile(category_name):
    return render_template('category-page.html', name="Меню")