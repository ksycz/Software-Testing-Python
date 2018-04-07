import unittest
from selenium import webdriver

class AutomationPractice(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://automationpractice.com")


    def test_open_new_account_form(self):
        self.singInBtn = self.driver.find_element_by_class_name("login")
        self.singInBtn.click()
        self.signInEmail = self.driver.find_element_by_id("email_create")
        self.signInEmail.send_keys("mynewemail@test.com")
        self.createAccountBtn = self.driver.find_element_by_name("SubmitCreate")
        self.createAccountBtn.click()
        self.driver.implicitly_wait(30)
        self.assertTrue(self.driver.find_element_by_id("customer_firstname"))

    def test_new_account_incorrect_email(self):
        self.singInBtn = self.driver.find_element_by_class_name("login")
        self.singInBtn.click()
        self.signInEmail = self.driver.find_element_by_id("email_create")
        self.signInEmail.send_keys("email")
        self.createAccountBtn = self.driver.find_element_by_name("SubmitCreate")
        self.createAccountBtn.click()
        self.incorrectEmailError = self.driver.find_element_by_css_selector("#create_account_error > ol > li").text
        self.assertEqual(incorrectEmailError, 'Invalid email address.')

    def test_main_search(self):
        self.searchInput = self.driver.find_element_by_id("search_query_top")
        self.searchInput.send_keys("dress")
        self.searchBtn = self.driver.find_element_by_name("submit_search")
        self.searchBtn.click()
        self.foundProduct = self.driver.find_element_by_class_name("product-name").lowercase
        self.assertContains(foundProduct, "dress")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
