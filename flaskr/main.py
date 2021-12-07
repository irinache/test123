from flask import Blueprint, render_template
from .db import get_db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/<lang>')
def index(lang='uk'):
    if lang not in ['en', 'ru', 'uk']:
        lang = 'uk'
    db = get_db()
    categories = db.execute("SELECT * FROM categories;").fetchall()
    theme = db.execute("SELECT value FROM config WHERE param='theme';").fetchall()
    if theme[0][0] == "light":
        theme_path = 'images/light-theme-images/'
    else:
        theme_path = 'images/dark-theme-images/'
    return render_template('categories-list.html', categories=categories, lang=lang, theme_path=theme_path, url="/")

@main.route('/category/<id>')
@main.route('/category/<id>/<lang>')
def open_category(id, lang='uk'):
    if lang not in ['en', 'ru', 'uk']:
        lang = 'uk'
    db = get_db()
    dishes = db.execute("SELECT * FROM dishes WHERE category_id = ?;", id).fetchall()
    category = db.execute("SELECT * FROM categories WHERE id=?;", id).fetchone()
    print(dishes)
    return render_template('category-page.html', dishes=dishes, category=category, lang=lang, url='/category/'+str(id)+'/')










