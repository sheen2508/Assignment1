from pymongo import MongoClient
import unittest

class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("mongodb+srv://sheen2508:fjvgfjyghytd5fch@cloud.mongodb.com/v2/673b8f48312f1b7d3e5e58/test")
        self.db = self.client['shop_db']

    def test_ping_database(self):
        # Verify database connection with a ping
        response = self.client.admin.command('ping')
        self.assertEqual(response['ok'], 1.0)  # Ping successful if 'ok' is 1.0

if __name__ == "__main__":
    unittest.main()
