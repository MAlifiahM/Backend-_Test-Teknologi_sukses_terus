import MySQLdb
from flask_restful import Resource
from .. import mysql
from ..utils.response import template_response


class AuthorBooksResource(Resource):
    @staticmethod
    def get(author_id):
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT a.name as author_name, a.birth_date, b.title as book_title, b.description as book_description, b.publish_date as book_publish_date FROM books b LEFT JOIN authors a on a.id = b.author_id WHERE b.author_id=%s", (author_id,))
            books = cur.fetchall()
            if len(books) is not 0:
                return template_response(message="Success get Author books",data=books)
            else:
                return template_response(message="Author books not found", response_code=404)
        except MySQLdb.Error as error:
            return template_response(message="Error : " + str(error), error=True, response_code=500)