from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class PracticePage(BasePage):
    first_name_field = (By.ID, 'firstName')
    last_name_field = (By.ID, 'lastName')
    email_name_field = (By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #userEmail')
    gender = (By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #gender-radio-2')
    mobile_number_field = (By.CSS_SELECTOR, 'div[class ="col-md-9 col-sm-12"] #userNumber')
    date_of_birth = (By.ID, 'dateOfBirthInput')
    date_of_birth2 = (By.CSS_SELECTOR, 'div [aria-label = "Choose Tuesday, November 14th, 2023"]')
    hobbies = (By.ID, 'hobbies-checkbox-1')
    submit_button = (By.ID, 'submit')
    submitting_form = (By.CLASS_NAME, 'modal-content')

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        return self.driver.get(url)

    def set_user_name(self, first_name):
        self.set(self.first_name_field, first_name)

    def set_last_name(self, last_name):
        self.set(self.last_name_field, last_name)

    def set_email_name(self, email_name):
        self.set(self.email_name_field, email_name)

    def set_mobile_number(self, mobile_number):
        self.set(self.mobile_number_field, mobile_number)

    def click_date_of_birth(self):
        self.click(self.date_of_birth)

    def click_date_of_birth2(self):
        self.click(self.date_of_birth2)

    def click_submit_button(self):
        self.driver.execute_script("document.getElementById('submit').style.marginTop = '-600px';")
        self.click(self.submit_button)

    def fill_practice_form_information(self, first_name, last_name, email_name, mobile_number):
        self.set_user_name(first_name)
        self.set_last_name(last_name)
        self.set_email_name(email_name)
        self.set_mobile_number(mobile_number)
        self.click_date_of_birth()
        self.click_date_of_birth2()
