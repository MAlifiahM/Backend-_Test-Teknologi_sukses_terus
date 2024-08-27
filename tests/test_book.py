import unittest
from unittest.mock import patch, MagicMock
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class TestBookResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch('app.resources.book.mysql')
    def test_get_book_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'id': 1, 'title': 'The Great Gatsby', 'author_id': 1, 'publish_date': '1925-04-10', 'description': 'A novel'}
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/books/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Success get book data', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_get_book_not_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/books/999')

        self.assertEqual(response.status_code, 404)
        self.assertIn('Book data is not found', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_get_all_books(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'id': 1, 'title': 'The Great Gatsby', 'author_id': 1, 'publish_date': '1925-04-10', 'description': 'A novel'},
            {'id': 2, 'title': 'To Kill a Mockingbird', 'author_id': 2, 'publish_date': '1960-07-11', 'description': 'A novel'}
        ]
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/books')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Success get all book data', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_post_book(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        data = json.dumps({
            'author_id': 1,
            'title': 'The Great Gatsby',
            'publish_date': '1925-04-10',
            'description': 'A novel'
        })
        response = self.app.post('/books', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn('Book created successfully', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_post_book_date_format_error(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor
        data = json.dumps({
            'author_id': 1,
            'title': 'The Great Gatsby',
            'publish_date': '28-01-2023',
            'description': 'A novel'
        })
        response = self.app.post('/books', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('wrong input date format should be yyyy-mm-dd', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_put_book(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        data = json.dumps({
            'author_id': 1,
            'title': 'The Great Gatsby',
            'publish_date': '1925-04-10',
            'description': 'A novel'
        })
        response = self.app.put('/books/1', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Book updated successfully', response.data.decode())

    @patch('app.resources.book.mysql')
    def test_delete_book(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.delete('/books/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Book deleted successfully', response.data.decode())


if __name__ == '__main__':
    unittest.main()