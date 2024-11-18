class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient("mongodb+srv://sheen2508:fjvgfjyghytd5fch@cloud.mongodb.com/v2/673b8f48312f1b7d3e5e58/test")
        self.db = self.client['shop_db']
        self.collection = self.db['products']

    def test_insert_document(self):
        test_document = {"name": "Test Product", "tag": "Test", "price": 20.99, "image_path": "static/images/test.jpg"}
        insert_result = self.collection.insert_one(test_document)

        fetched_document = self.collection.find_one({"_id": insert_result.inserted_id})
        self.assertIsNotNone(fetched_document)
        self.assertEqual(fetched_document['name'], "Test Product")

if __name__ == "__main__":
    unittest.main()
