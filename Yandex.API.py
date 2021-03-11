import unittest
import requests
from main import upload_file
token = input("Введите токен")

class TestFooYaUploader(unittest.TestCase):
    def setUp(self):
        print("method setup")

    def tearDown(self):
        print("method setup")

    def test_upload_file(self):
        import requests
        upload_file("Fight", token)
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/files", params={"limit": 1000},
                                headers={"Authorization": token})
        response.raise_for_status()
        response_1 = response.json()
        list_of_files = []
        for element in response_1["items"]:
            list_of_files.append(element["name"])
        self.assertIn("Fight", list_of_files)

    def test_wrong_upload_file(self):
        import requests
        upload_file("Fight", token)
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/files", params={"limit": 1000},
                                headers={"Authorization": token})
        response.raise_for_status()
        response_1 = response.json()
        list_of_files = []
        for element in response_1["items"]:
            list_of_files.append(element["name"])
        self.assertIn("Fight", list_of_files)

if __name__ == '__main__':
    unittest.main()




