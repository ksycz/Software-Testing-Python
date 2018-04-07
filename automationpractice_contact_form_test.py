import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class AutomationPractice(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://automationpractice.com/index.php?controller=contact")

    def test_contact_form_open(self):
        self.contactUs = self.driver.find_element_by_id('contact-link')
        self.contactUs.click()
        self.contactForm = self.driver.find_element_by_class_name('contact-form-box')
        self.assertTrue(self.contactForm)

    def test_contact_form_full(self):
        self.subject = self.driver.find_element_by_id('id_contact')
        self.select = Select(self.subject)
        self.select.select_by_value('2')
        self.email = self.driver.find_element_by_id('email')
        self.email.send_keys('test@test.com')
        self.order = self.driver.find_element_by_id('id_order')
        self.order.send_keys("OR12345")
        self.message = self.driver.find_element_by_id('message')
        self.message.send_keys("This is a testing message")
        self.sendBtn = self.driver.find_element_by_id('submitMessage')
        self.sendBtn.click()
        self.successMessage = self.driver.find_element_by_class_name('alert-success').text
        self.assertEqual(self.successMessage, 'Your message has been successfully sent to our team.')

    def test_contact_form_incorrect_email(self):
        self.subject = self.driver.find_element_by_id('id_contact')
        self.select = Select(self.subject)
        self.select.select_by_value('2')
        self.email = self.driver.find_element_by_id('email')
        self.email.send_keys('test')
        self.order = self.driver.find_element_by_id('id_order')
        self.order.send_keys("OR12345")
        self.message = self.driver.find_element_by_id('message')
        self.message.send_keys("This is a testing message")
        self.sendBtn = self.driver.find_element_by_id('submitMessage')
        self.sendBtn.click()
        self.errorMessage = self.driver.find_element_by_css_selector('#center_column > div > ol > li').text
        self.assertEqual(self.errorMessage, 'Invalid email address.')

        def tearDown(self):
          self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
      