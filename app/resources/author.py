from datetime import datetime
import MySQLdb
from flask import request
from flask_restful import Resource
from .. import mysql
from ..utils.response import template_response


class AuthorResource(Resource):
    @staticmethod
    def get(author_id=None):
        try:
            cur = mysql.connection.cursor()
            if author_id:
                cur.execute("SELECT * FROM authors WHERE id=%s", (author_id,))
                author = cur.fetchone()
                if author is not None:
                    return template_response(message="Success get author data", data=author)
                else:
                    return template_response(message="Author data not found", response_code=404)
            else:
                cur.execute("SELECT * FROM authors")
                authors = cur.fetchall()
                if authors is not None:
                    return template_response(message="Success get all author data", data=authors)
                else:
                    return template_response(message="Author data not found", response_code=404)
        except MySQLdb.Error as error:
            return template_response(message="Error : " + str(error), error=True, response_code=500)

    @staticmethod
    def post():
        data = request.get_json()
        try :
            datetime.strptime(data['birth_date'], '%Y-%m-%d')
        except ValueError:
            return template_response("wrong input date format should be yyyy-mm-dd", error=True, response_code=400)

        cur = mysql.connection.cursor()

        try:
            cur.execute("INSERT INTO authors (name, bio, birth_date) VALUES (%s, %s, %s)",
                        (data['name'], data['bio'], data['birth_date']))
            mysql.connection.commit()
            return template_response(message="Author created successfully", response_code=201)
        except MySQLdb.Error as error :
            return template_response(message="Error : " + str(error), error=True, response_code=500)

    @staticmethod
    def put(author_id):
        data = request.get_json()
        try:
            datetime.strptime(data['birth_date'], "%Y-%m-%d")
        except ValueError:
            return template_response("wrong input date format should be yyyy-mm-dd", error=True, response_code=400)

        cur = mysql.connection.cursor()

        try:
            cur.execute("UPDATE authors SET name=%s, bio=%s, birth_date=%s WHERE id=%s",
                        (data['name'], data['bio'], data['birth_date'], author_id))
            mysql.connection.commit()
            return template_response(message="Author updated successfully")
        except MySQLdb.Error as error:
            template_response(message="Error : " + str(error), error=True, response_code=500)

    @staticmethod
    def delete(author_id):
        cur = mysql.connection.cursor()
        try:
            cur.execute("DELETE FROM authors WHERE id=%s", (author_id,))
            mysql.connection.commit()
            return template_response(message="Author deleted successfully")
        except MySQLdb.Error as error:
            return template_response(message="Error : " + str(error), error=True, response_code=500)
