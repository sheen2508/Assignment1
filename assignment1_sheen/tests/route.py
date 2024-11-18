import unittest
from app import app  # Import your Flask application

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Flask test client

    def test_invalid_method(self):
        # Test invalid POST request on a GET route
        response = self.app.post('/mongodb+srv://sheen2508:fjvgfjyghytd5fch@cloud.mongodb.com/v2/673b8f48312f1b7d3e5e58/test') 
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()
