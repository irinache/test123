from flask import *
from .db import get_db
from flask_login import login_required, login_user, logout_user
from .models import *

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET"])
def login():
    return render_template('admin/login.html')

@auth.route('/login', methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.get_by_credentials(username, password)
#query.filter_by(username=username).first()
    if not user: # or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    login_user(user)
    return redirect(url_for('auth.admin_index'))

@auth.route("/logout")
@login_required
def logout():
    logout_user(current-user)
    return redirect(url_for("main.index"))

@auth.route("/admin")
@login_required
def admin_index():
    return render_template('admin/index.html')

@auth.route("/admin/categories")
@login_required
def admin_categories():
    db = get_db()
    theme = db.execute("SELECT value FROM config WHERE param='theme';").fetchall()
    if theme[0][0] == "light":
        theme_path = 'images/light-theme-images/'
    else:
        theme_path = 'images/dark-theme-images/'
    images = db. execute("SELECT * FROM images;")
    return render_template('admin/categories.html', images=images, theme_path=theme_path)

@auth.route("/admin/settings")
@login_required
def settings():
    return "<h1>Route protected</h1>"

@auth.route("/admin/_categories", methods=["GET"])
#login_required
def category():
    db = get_db()
    theme = db.execute("SELECT value FROM config WHERE param='theme';").fetchall()
    if theme[0][0] == "light":
        theme_path = 'images/light-theme-images/'
    else:
        theme_path = 'images/dark-theme-images/'
    cats = db.execute("SELECT id, name_en, name_uk, name_ru, image FROM categories;")
    response = []
    for (id, name_en, name_uk, name_ru,image) in cats:
        image_url = url_for('static', filename=theme_path+image)
        response.append(dict({ "id": id, "name_en": name_en, "name_uk": name_uk, "name_ru": name_ru, "image_url": image_url }))
    return jsonify(response)

@auth.route("/admin/_categories", methods=["POST"])
#login_required
def category_post():
    db = get_db()
    data = request.form["data"]
"""
#    if data:
#        records = db.execute("SELECT * FROM dishes;").fetchall()
#        dishes = []
#        for (id, title_en, title_ru, title_uk, price, category_id) in records:
#            dishes.append(dict({ "id": id,
#                       "title_en": title_en,
#                       "title_ru": title_ru,
#                       "title_uk": title_uk,
#                       "price": price,
#                       "category_id": category_id}))
#        records2 = db.execute("SELECT * FROM categories;").fetchall()
#        categories = []
#        for (id, name_en, name_ru, name_uk, image) in records2:
#            categories.append(dict({
#                "id": id,
#                "name_en": name_en,
#                "name_ru": name_ru,
#                "name_uk": name_uk,
#                "image": image }))
#        db.execute("DELETE FROM dishes;")
#        db.execute("DELETE FROM categories;")
#        for ct in data:
#            if "id" in ct:
#                for ct2 in categories:
#                    if ct2["id"] == ct["id"]:
#                        ct["image"] = ct2["image"]
#                        break
#            db.execute("INSERT INTO categories (name_en, name_ru, name_uk, images) VALUES ('"+ct["name_en"]+"','"+ct["name_ru"]+"','"+ct["name_uk"]+"','"+ct["image"]+"';)")
#            id = db.execute("SELECT MAX(id) FROM categories;").fetchone()
#            if id:
#                db.execute("INSERT INTO dishes (title_en, title_ru, title_uk, price, category_id) VALUES (
"""
#    return jsonify({ "status": "ok" })

@auth.route("/admin/_menu", methods=["GET"])
#login_required
def menu():
    db = get_db()
    menu = db.execute("SELECT c.name_en as category_en, c.name_uk as category_uk, c.name_ru as category_ru, d.title_en as title_en, d.title_uk as title_uk, d.title_ru as title_ru, d.price as price FROM dishes as d JOIN categories as c ON d.category_id=c.id").fetchall()
    response = []
    for (category_en, category_uk, category_ru, title_en, title_uk, title_ru, price) in menu:
        response.append(dict({ 'category_en': category_en, 'category_uk': category_uk, 'category_ru': category_ru, 'title_en': title_en, 'title_uk': title_uk, 'title_ru': title_ru, 'price': price  }))
    return jsonify(response)

@auth.route("/admin/_menu", methods=["POST"])
def menu_post():
    db = get_db()
#    menu = request.json["menu"]
#    for row in menu:
#        db.execute("INSERT INTO ")
