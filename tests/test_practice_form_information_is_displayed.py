from selenium.webdriver.common.by import By
from PageObject.practice_page import PracticePage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestPracticeForm(BaseTest):
    def test_practice_form_information_is_displayed(self):
        practice_page = PracticePage(self.driver)
        practice_page.open_page(TestData.practice_form_url)
        practice_page.fill_practice_form_information(
            'Igor', 'Ivanov', 'igor@example.com', '6532489752'
        )
        gender_field = practice_page.find(By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #gender-radio-2')
        self.driver.execute_script("arguments[0].checked = true;", gender_field)
        hobbies_field = practice_page.find(By.ID, 'hobbies-checkbox-1')
        self.driver.execute_script("arguments[0].checked = true;", hobbies_field)
        practice_page.click_submit_button()
        # to do Find and display function doesn't work
        #submitting_form = practice_page.find(By.CLASS_NAME, 'modal-content')
        assert practice_page.form_is_displayed()

    # def test_practice_form_information_is_displayed():
    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # browser.get('https://demoqa.com/automation-practice-form')
    # first_name = browser.find_element(By.ID, 'firstName')
    # firstName = 'Igor'
    # first_name.send_keys(firstName)
    # last_name = browser.find_element(By.ID, 'lastName')
    # lastName = 'Ivanov'
    # last_name.send_keys(lastName)
    # email_name = browser.find_element(By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #userEmail')
    # emailName = 'igor@example.com'
    # email_name.send_keys(emailName)
    # gender = browser.find_element(By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #gender-radio-2')
    # browser.execute_script("arguments[0].checked = true;", gender)
    # mobile_number = browser.find_element(By.CSS_SELECTOR, 'div[class ="col-md-9 col-sm-12"] #userNumber')
    # mobile_number.send_keys('6532489752')
    # date_of_birth = browser.find_element(By.ID, 'dateOfBirthInput')
    # date_of_birth.click()
    # date_of_birth2 = browser.find_element(By.CSS_SELECTOR, 'div [aria-label = "Choose Tuesday, October 10th, 2023"]')
    # date_of_birth2.click()
    # hobbies = browser.find_element(By.ID, 'hobbies-checkbox-1')
    # browser.execute_script("arguments[0].checked = true;", hobbies)
    # submit_button = browser.find_element(By.ID, 'submit')
    # browser.execute_script("document.getElementById('submit').style.marginTop = '-600px';")
    # submit_button.click()
    # submitting_form = browser.find_element(By.CLASS_NAME, 'modal-content')
    # assert submitting_form.is_displayed()
    #
    # def test_that_form_has_red_columns():
    # browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    # browser.get('https://demoqa.com/automation-practice-form')
    # submit_button = browser.find_element(By.ID, 'submit')
    # browser.execute_script("document.getElementById('submit').style.marginTop = '-600px';")
    # submit_button.click()
    # first_name = browser.find_element(By.ID, 'firstName')
    # first_name_value = first_name.get_attribute("style")
    # assert first_name_value.borderColor == '#dc3545'
