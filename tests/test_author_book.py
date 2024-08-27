import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class TestAuthorBookResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch('app.resources.author_books.mysql')
    def test_get_author_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'author_name': 'John', 'birth_date': '1980-01-01', 'book_title': 'The Great Gatsby', 'book_description': 'A novel', 'book_publish_date': '1925-04-10'},
            {'author_name': 'John', 'birth_date': '1980-01-01', 'book_title': 'To Kill a Mockingbird', 'book_description': 'A novel', 'book_publish_date': '1960-07-11'}
        ]
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/authors/1/books')

        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Success get Author books', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_get_author_not_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/authors/999/books')

        self.assertEqual(response.status_code, 404)
        self.assertIn('Author books not found', response.data.decode())


if __name__ == '__main__':
    unittest.main()