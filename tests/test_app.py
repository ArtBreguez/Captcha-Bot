import unittest
from flask import Flask
from flask.testing import FlaskClient
import os
import sys

current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(root_dir)
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client: FlaskClient = self.app.test_client()

    def test_predict(self):
        with open('tests/image_base64.txt', 'r') as image_file:
            base64_image = image_file.read()

        response = self.client.post('/predict', json={'image': base64_image})

        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        prediction = result.get('prediction')
        self.assertIsNotNone(prediction)
        self.assertEqual(prediction, '1a1sZ')

if __name__ == '__main__':
    unittest.main()
