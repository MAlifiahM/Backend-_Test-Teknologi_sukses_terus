from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Api
from .config import Config

mysql = MySQL()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)

    from .resources.author import AuthorResource
    from .resources.book import BookResource
    from .resources.author_books import AuthorBooksResource

    api = Api(app)
    api.add_resource(AuthorResource, '/authors', '/authors/<int:author_id>')
    api.add_resource(BookResource, '/books', '/books/<int:book_id>')
    api.add_resource(AuthorBooksResource, '/authors/<int:author_id>/books')

    return app
