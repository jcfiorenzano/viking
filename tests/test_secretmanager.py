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
    
    def test_deletesecret(self):
        site_url = "http://test.com"
        SecretFileManager.delete = create_autospec(SecretFileManager.delete)

        SecretManager.delete(site_url)

        SecretFileManager.delete.assert_called_once_with(site_url)


if __name__ == '__main__':
    unittest.main()