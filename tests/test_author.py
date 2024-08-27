import unittest
from unittest.mock import patch, MagicMock
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class TestAuthorResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch('app.resources.author.mysql')
    def test_get_author_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'id': 1, 'name': 'John', 'bio': 'An author bio', 'birth_date': '1980-01-01'}
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/authors/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Success get author data', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_get_author_not_found(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/authors/999')

        self.assertEqual(response.status_code, 404)
        self.assertIn('Author data not found', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_get_all_authors(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'John', 'bio': 'An author bio', 'birth_date': '1980-01-01'}, {'id': 2, 'name': 'Jane', 'bio': 'An author bio', 'birth_date': '1980-01-01'}]
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.get('/authors')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Success get all author data', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_post_author(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        data = json.dumps({
            'name': 'John',
            'bio': 'An author bio',
            'birth_date': '1980-01-01'
        })
        response = self.app.post('/authors', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn('Author created successfully', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_post_author_date_format_error(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor
        data = json.dumps({
            'name': 'John',
            'bio': 'An author bio',
            'birth_date': '28-01-2020'
        })
        response = self.app.post('/authors', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('wrong input date format should be yyyy-mm-dd', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_put_author(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        data = json.dumps({
            'name': 'John Updated',
            'bio': 'Updated bio',
            'birth_date': '1980-01-01'
        })
        response = self.app.put('/authors/1', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Author updated successfully', response.data.decode())

    @patch('app.resources.author.mysql')
    def test_delete_author(self, mock_mysql):
        mock_cursor = MagicMock()
        mock_mysql.connection.cursor.return_value = mock_cursor

        response = self.app.delete('/authors/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Author deleted successfully', response.data.decode())


if __name__ == '__main__':
    unittest.main()