from selenium import webdriver
import unittest

username = "codechallenge"
password = "Password123"
url = "https://clarity.dexcom.com"

class DexcomTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver=webdriver.Chrome(executable_path="C:\\Users\\laura\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
            cls.driver.maximize_window()

        def test_homePageTitle(self):
            self.driver.get(url)
            self.assertEqual("Dexcom CLARITY",self.driver.title,"webpage title is not matching")

        def test_login(self):
            self.driver.find_element_by_xpath("//a[@href='/users/auth/dexcom_sts']").click()
            self.driver.find_element_by_name("username").send_keys(username)
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
            self.assertEqual("Dexcom CLARITY", self.driver.title, "webpage title is not matching")

        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
