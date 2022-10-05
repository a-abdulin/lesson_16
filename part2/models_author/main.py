# Напишите модели автор(Author) и книга (Book)
# в соответствии с uml (схема в файле tables.png в папке задания)
#
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "author"
    # TODO добавьте поля модели здесь
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)


class Book(db.Model):
    __tablename__ = "book"
    # TODO добавьте поля модели здесь
    id=Column(Integer, primary_key=True)
    title=Column(String)
    copy_right=Column(Integer)
    author_id=(Integer, ForeignKey('author.id'))
    author=relationship("Author")

# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели


db.create_all()
session = db.session()
cursor_author = session.execute("SELECT * from author").cursor
mytable = prettytable.from_db_cursor(cursor_author)
cursor_book = session.execute("SELECT * from book").cursor
mytable2 = prettytable.from_db_cursor(cursor_book)

if __name__ == '__main__':
    print(mytable)
    print(mytable2)
