DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS dishes;
DROP TABLE IF EXISTS config;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS images;

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_en TEXT UNIQUE NOT NULL,
  name_ru TEXT UNIQUE NOT NULL,
  name_uk TEXT UNIQUE NOT NULL,
  image TEXT NOT NULL
);

CREATE TABLE dishes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title_en TEXT NOT NULL,
  title_ru TEXT NOT NULL,
  title_uk TEXT NOT NULL,
  price INTEGER NOT NULL,
  category_id INTEGER NOT NULL,
  FOREIGN KEY (category_id) REFERENCES categories (id)
);

CREATE TABLE config (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
    param TEXT UNIQUE NOT NULL,
    value TEXT NOT NULL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  admin BOOLEAN NOT NULL
);

CREATE TABLE images (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  image TEXT NOT NULL
);

insert into categories (name_en, name_ru, name_uk, image) values ("Barbecue", "Гриль", "Гриль", "Grill.png");
insert into categories (name_en, name_ru, name_uk, image) values ("Meat", "Мясо", "М'ясо", "Meat.png");

insert into dishes (title_en, title_ru, title_uk, price, category_id) values ("", "", "Яловичі щічки з картопляним пюре", "360", 2);
insert into dishes (title_en, title_ru, title_uk, price, category_id) values ("", "", "Філе курча на рожевому кус-кусі", "220", 2);
insert into dishes (title_en, title_ru, title_uk, price, category_id) values ("", "", "Лосось", "350", 1);
insert into dishes (title_en, title_ru, title_uk, price, category_id) values ("", "", "Дорадо", "110", 1);

insert into config(param, value) values ("theme", "light");
insert into users(username, password, admin) values ("admin", "12345", 1);

insert into images(title, image) values ("Гриль", "Grill.png"),
                                        ("Мясо", "Meat.png"),
                                        ("Гарниры", "Garnish.png"),
                                        ("Десерты", "Dessert.png"),
                                        ("Холодные закуски", "Cold_snaks.png"),
                                        ("Горячие закуски", "Hot_appetizers.png"),
                                        ("Рыба", "Fish.png"),
                                        ("Супы", "Soup.png"),
                                         ("Паста и ризотто", "Sushi.png"),
                                         ("Филадельфия роллы", "Sushi.png"),
                                         ("Теплые темпурные роллы", "Sushi.png"),
                                         ("Маки роллы", "Sushi.png"),
                                         ("Сашими", "Sashimi.png"),
                                         ("Фирменные роллы", "Sushi.png"),
                                         ("Салаты", "Salad.png"),
                                         ("Калифорния роллы", "Sushi.png");





