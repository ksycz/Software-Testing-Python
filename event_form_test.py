#importing needed modules
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


# test scenario 1 - checking the basic functionality of all fields one by one
class FieldsTest(unittest.TestCase):
    def setUp(self):
        "Sets up the web driver"
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.123contactform.com/form-3079673/Events-Form")
        self.driver.maximize_window()

    def test_drop_down(self):
        "Tests if an item from the drop-down menu is selectable"
        driver = self.driver
        for i in range(5):
            try:
                # Locate the Sector and create a Select object
                select_element = Select(driver.find_element_by_id('id123-control33865791'))
                select_element.select_by_value('Collaboration')
                break
            except NoSuchElementException as e:
                print("Retry")
                time.sleep(1)
        else:
            print("Drop-down fail")

        self.driver.quit()


    def test_first_name(self):
        "Tests if some data can be inserted into the First name field and there is no validation error when submitting the form"
        driver = self.driver
        firstName = 'Jane'

        submitButtonTagName = 'button'
        firstNameID = 'id123-control33873733'
        firstNameFilledIn = "id123-control33873733" and "no-validation-error" #I look for ID and validation class

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(firstNameID))
        emailFieldElement.send_keys(firstName)
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name(submitButtonTagName))
        submitButtonElement.click()
        # checking if the validated First name field exists on the page
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name(firstNameFilledIn))

        self.driver.quit()

    def test_last_name(self):
        "Tests if some data can be inserted into the First name field and there is no validation error when submitting the form"
        driver = self.driver
        lastName = 'Doe'

        submitButtonTagName = 'button'
        lastNameID = 'id123-control33873751'
        lastNameFilledIn = 'id123-control33873751' and 'no-validation-error' #I look for ID and validation class

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(lastNameID))
        emailFieldElement.send_keys(lastName)
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name(submitButtonTagName))
        submitButtonElement.click()
        # checking if the validated Last name field exists on the page
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name(lastNameFilledIn))

        self.driver.quit()


    def test_email_correct(self):
        "Tests if a correct email does not return an validation error and can be submitted"
        driver = self.driver
        eventFormEmail = 'test@domain.com'

        emailFieldID = 'id123-control33865730'
        submitButtonTagName = 'button'
        emailFieldFilledIn = 'id123-control33873733' and 'no-validation-error' #I look for ID and validation class
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        emailFieldElement.send_keys(eventFormEmail)
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name(submitButtonTagName))
        submitButtonElement.click()
        # checking if the validated Email name field exists on the page
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name(emailFieldFilledIn))

        self.driver.quit()


    def test_email_incorrect(self):
        "Tests if an incorrect email does return an validation error and cannot be submitted"
        driver = self.driver
        Email = 'testdomain.com' #missing '@'

        emailFieldID = 'id123-control33865730'
        submitButtonTagName = 'button'
        emailFieldFilledInIncorrect = 'id123-fielderror33865730'

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        emailFieldElement.send_keys(Email)
        submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_tag_name(submitButtonTagName))
        submitButtonElement.click()
        # checking if the field error appears for the Email field
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldFilledInIncorrect))

        self.driver.quit()

    def test_select_checkboxes(self):
        "Tests if each checkbox is selectable"
        driver = self.driver
        for i in range(5):
            try:
                driver.find_element_by_css_selector('label[for=id123-control33865757_0]').click()
                driver.find_element_by_css_selector('label[for=id123-control33865757-1]').click()
                driver.find_element_by_css_selector('label[for=id123-control33865757-2]').click()
                driver.find_element_by_css_selector('label[for=id123-control33865757-3]').click()
                driver.find_element_by_css_selector('label[for=id123-control33865757-4]').click()
                driver.find_element_by_css_selector('label[for=id123-control33865757-5]').click()
                break
            except NoSuchElementException as e:
                print("Retry")
                time.sleep(1)
        else:
            print("Checkbox fail")

        self.driver.quit()

    def test_select_radio_button(self):
        "Tests if a radio button is selectable"
        driver = self.driver
        for i in range(5):
            try:
                driver.find_element_by_id('id123-control33865740_2').click()
                break
            except NoSuchElementException as e:
                print("Retry")
                time.sleep(1)
        else:
            print("Radio button fail")

        self.driver.quit()

# test scenario 2 - checking the form submission
class SubmissionTest(unittest.TestCase):
    @classmethod
    # set up method
    def setUp(self):
        "Sets up the web driver"
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.123contactform.com/form-3079673/Events-Form")
        self.driver.maximize_window()

    def test_submission_correct(self):
        "Tests if the form can be submitted when the required fields are filled in with correct data"
        driver = self.driver
        eventFormFirstName = 'Honza'
        eventFormLastName = 'Novak'
        eventFormEmail = 'hn_test@domain.com'

        firstNameFieldName = 'control33873733'
        lastNameFieldID = 'id123-control33873751'
        emailFieldID = 'id123-control33865730'
        submitButtonTagName = 'button'
        thankYouPageLinkText = 'Please click here to continue.'

        firstNameFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(firstNameFieldName))
        lastNameFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(lastNameFieldID))
        emailFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(emailFieldID))
        submitButtonElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_tag_name(submitButtonTagName))

        firstNameFieldElement.send_keys(eventFormFirstName)
        lastNameFieldElement.send_keys(eventFormLastName)
        emailFieldElement.send_keys(eventFormEmail)
        submitButtonElement.click()
        # checking if the form was sent = checking if the link with the text 'Please click here to continue.' is visible on the page
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_link_text(thankYouPageLinkText))

        self.driver.quit()

    def test_submission_incorrect(self):
        "Tests if the form can be submitted with incorrect data"
        driver = self.driver
        eventFormFirstName = 'Honza'
        eventFormEmail = 'test@'

        firstNameFieldName = 'control33873733'
        emailFieldID = 'id123-control33865730'
        submitButtonTagName = 'button'
        failMessageID = 'errormsgDialogMessage'

        firstNameFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(firstNameFieldName))
        emailFieldElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(emailFieldID))
        submitButtonElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_tag_name(submitButtonTagName))

        firstNameFieldElement.send_keys(eventFormFirstName)
        emailFieldElement.send_keys(eventFormEmail)
        submitButtonElement.click()
        # checking if the form was not sent = checking if the submitting fail message appears
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(failMessageID))

        self.driver.quit()

    def test_submission_blank(self):
        "Tests if the form does not validate when a required field is blank"
        driver = self.driver

        firstNameFieldBlankID = 'id123-fielderror33873733'
        lastNameFieldBlankID = 'id123-fielderror33873751'
        emailFieldBlankID = 'id123-fielderror33865730'
        submitButtonBlankFieldsTagName = 'button'

        submitButtonBlankFieldsElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_tag_name(submitButtonBlankFieldsTagName))
        submitButtonBlankFieldsElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(
            firstNameFieldBlankID or lastNameFieldBlankID or emailFieldBlankID))

        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
