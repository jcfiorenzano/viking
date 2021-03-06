import unittest
from unittest.mock import Mock
from unittest.mock import create_autospec
from viking.model.secret import Secret
import viking.file_manager.secret_file_manager as SecretFileManager
import viking.secret_manager.secret_manager as SecretManager

class TestSecretManager(unittest.TestCase):

    def test_getsecret(self):
        site_url = "http://test.com"
        expected_secret = Secret(site_url, "test-user", "test-password")
        expected_dictionary = { site_url: expected_secret}
        SecretFileManager.load = Mock(return_value= expected_dictionary)
        
        result = SecretManager.get(site_url)
        
        self.assertEqual(result, expected_secret)

    def test_getsecret_secret_no_exist(self):
        SecretFileManager.load = Mock(return_value= {})
        self.assertIsNone(SecretManager.get("this site does not exist"))


    def test_getallsecret(self):
        secret = Secret("http://test.com", "test-user", "test-password")
        dictionary = { "http://test.com": secret}
        expected_result = [secret]
        SecretFileManager.load = Mock(return_value= dictionary)
        
        result = SecretManager.get_all()

        self.assertEqual(result, expected_result)
    
    def test_addsecret(self):
        secret = Secret("http://test.com", "test-user", "test-password")
        SecretFileManager.save = create_autospec(SecretFileManager.save)

        SecretManager.add(secret)

        SecretFileManager.save.assert_called_once_with(secret)
    
    def test_add_nullvalue_raise_exception(self):
        with self.assertRaises(ValueError):
            SecretManager.add(None)
    
    def test_add_missing_required_values_raise_exception(self):
        with self.assertRaises(ValueError):
            SecretManager.add(Secret(site=None, username="username", password="password"))

        with self.assertRaises(ValueError):
            SecretManager.add(Secret(site="site", username=None, password="password"))
        
        with self.assertRaises(ValueError):
            SecretManager.add(Secret(site="site", username="username", password=None))
            
    def test_deletesecret(self):
        site_url = "http://test.com"
        SecretFileManager.delete = create_autospec(SecretFileManager.delete)

        SecretManager.delete(site_url)

        SecretFileManager.delete.assert_called_once_with(site_url)

    def test_search(self):
        secret_dictionary = {
            "https://www.mysite.com": Secret("https://www.mysite.com","username","password"),
            "https://www.othersite.com": Secret("https://www.othersite.com", "username", "password"),
            "yoursite": Secret("yoursite", "username", "password")
        }
        SecretFileManager.load = Mock(return_value= secret_dictionary)

        results = SecretManager.search("site")
        self.assertEqual(len(results), 3)

        results = SecretManager.search("mysite")
        self.assertEqual(len(results), 1)

        results = SecretManager.search("https")
        self.assertEqual(len(results), 2)

        results = SecretManager.search("sete")
        self.assertEqual(len(results), 0, "Non existed keyword")


if __name__ == '__main__':
    unittest.main()