# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

valid_first_name = "John"
valid_last_name = "Doe"
mobile_number = "042123456789"
invalid_email = "john.doe.com"
password = "Abc123?"
# Creating a class that inherits from the TestCase class from unittest
class WizzairRegistration(unittest.TestCase):

    # Runs before tests
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.set_page_load_timeout(2)
        self.driver.maximize_window()

    # Needs to contain test in the name
    def test_invalid_email(self):
        driver = self.driver
        loginBtn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
        loginBtn.click()
        # registerLink = self.driver.find_element_by_css_selector("#login-modal > form > div > p > button")
        registerLink = driver.find_element_by_xpath('//button[contains(text(), "Rejestracja")]')
        registerLink.click()
        firstNameInput = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        firstNameInput.send_keys(valid_first_name)
        lastNameInput = driver.find_element_by_css_selector("input[placeholder=Nazwisko]")
        lastNameInput.send_keys(valid_last_name)
        genderWoman = driver.find_element_by_css_selector("label[for=register-gender-female]")
        genderWoman.click()
        # force clicking
        driver.execute_script("arguments[0].click()", genderWoman)
        mobileNumber = driver.find_element_by_css_selector("input[type=tel]")
        mobileNumber.send_keys(mobile_number)
        # invalidEmail = driver.find_element_by_css_selector("input[data-test=booking-register-email]")
        # invalidEmail.send_keys(invalid_email)
        passwordInput = driver.find_element_by_css_selector("input[data-test=booking-register-password]")
        passwordInput.send_keys(password)
        country = driver.find_element_by_css_selector("input[data-test=booking-register-country]")
        country.click()
        countryPoland = driver.find_element_by_xpath("//*[@class='register-form__country-container__locations']/label[164]")
        countryPoland.location_once_scrolled_into_view
        countryPoland.click()
        privacyPolicy = driver.find_element_by_css_selector("label[for=registration-privacy-policy-checkbox]")
        privacyPolicy.click()
        registerBtn = driver.find_element_by_css_selector("button[data-test=booking-register-submit]")
        registerBtn.click()
        errorInvalidEmail = driver.find_element_by_xpath("//*[@id='regmodal-scroll-hook-4']/div[2]/span")
        # print(errorInvalidEmail.text)
        # assert errorInvalidEmail.is_displayed()
        self.assertEqual(errorInvalidEmail.text, 'Wpisz adres e-mail')


    # Runs after each tests
    def tearDown(self):
        self.driver.quit()

# parametr name
if __name__ == "__main__":
    unittest.main(verbosity = 2)
