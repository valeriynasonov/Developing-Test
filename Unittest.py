import unittest
from main import search_name, add_document, del_document
class TestFooDocumentsDirectories(unittest.TestCase):
    def setUp(self):
        print("method setup")

    def tearDown(self):
        print("method setup")

    def test_search_name(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.assertEqual(search_name(documents, "11-2"), "Геннадий Покемонов")

    def test_add_document(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }
        result = add_document(documents, directories, "1", "43", "Военный билет", "Геннадий Гудков")
        self.assertIn(result, 43)

    if __name__ == '__main__':
        unittest.main()