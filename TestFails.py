import unittest
from main import upload_file
token = input("Введите токен")
class TestFails(unittest.TestCase):
    def test_wrong_upload_file(self):
        import requests
        upload_file("Fight", token)
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/files", params={"limit": 1000},
                                headers={"Authorization": token})
        status_code = response.status_code
        self.assertNotEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()


