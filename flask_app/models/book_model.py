from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint
from flask_app.models import user_model
from flask_app.controllers import books_controller
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Book:
    DB = "personal_library"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.isbn = data['isbn']
        self.book_cover_image = data['book_cover_image']
        self.genre = data['genre']
        self.review = data['review']
        self.location = data['location']
        self.faavorite_quote = data['favorite_quote']
        self.recommend = data['recommend']
        self.on_loan = data['on_loan']
        self.loaned_to = data['loaned_to']
        self.date_loaned = data['date_loaned']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None


# get all books with one user's info
    @classmethod
    def get_all_books_from_one_user(cls):
        query = """
                SELECT * FROM books
                """
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

# can't figure out how to query specific user_id by using the session id.

# try geting all books but on the HTML side have an if statment. If the user_id is not in current session, don't show it.