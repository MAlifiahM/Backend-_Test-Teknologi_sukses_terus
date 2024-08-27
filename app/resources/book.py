from datetime import datetime
import MySQLdb
from flask import request
from flask_restful import Resource
from .. import mysql
from ..utils.response import template_response


class BookResource(Resource):
    @staticmethod
    def get(book_id=None):
        try:
            cur = mysql.connection.cursor()
            if book_id:
                cur.execute("SELECT * FROM library_db.books WHERE id=%s", (book_id,))
                book = cur.fetchone()
                if book is not None:
                    return template_response("Success get book data", book)
                else:
                    return template_response("Book data is not found", response_code=404)
            else:
                cur.execute("SELECT * FROM books")
                books = cur.fetchall()
                if books is not None:
                    return template_response("Success get all book data", books)
                else:
                    return template_response("Book data is not found", response_code=404)
        except MySQLdb.Error as error:
            return template_response(message="Error : " + str(error), error=True, response_code=500)

    @staticmethod
    def post():
        data = request.get_json()
        try :
            datetime.strptime(data['publish_date'], '%Y-%m-%d')
        except ValueError:
            return template_response("wrong input date format should be yyyy-mm-dd", error=True, response_code=400)

        cur = mysql.connection.cursor()

        try :
            cur.execute("INSERT INTO books (title, description, publish_date, author_id) VALUES (%s, %s, %s, %s)",
                        (data['title'], data['description'], data['publish_date'], data['author_id']))
            mysql.connection.commit()
            return template_response(message="Book created successfully", response_code=201)
        except MySQLdb.Error as error :
            return template_response(error=True, message="Error : " + str(error), response_code=500)
        finally:
            cur.close()

    @staticmethod
    def put(book_id):
        data = request.get_json()

        try :
            datetime.strptime(data['publish_date'], '%Y-%m-%d')
        except ValueError:
            return template_response("wrong input date format should be yyyy-mm-dd", error=True, response_code=400)

        cur = mysql.connection.cursor()

        try :
            cur.execute("UPDATE books SET title=%s, description=%s, publish_date=%s, author_id=%s WHERE id=%s",
                        (data['title'], data['description'], data['publish_date'], data['author_id'], book_id))
            mysql.connection.commit()
            return template_response(message="Book updated successfully")
        except MySQLdb.Error as error :
            return template_response(message="Error : " + str(error), error=True, response_code=500)
        finally:
            cur.close()

    @staticmethod
    def delete(book_id):
        cur = mysql.connection.cursor()
        try:
            cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
            mysql.connection.commit()
            return template_response(message="Book deleted successfully")
        except MySQLdb.Error as error:
            return template_response(message="Error : " + str(error), error=True, response_code=500)
