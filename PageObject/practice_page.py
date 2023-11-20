from PageObject.base_page import BasePage
from Locators.practice_form_locators import PracticeFormLocators


class PracticePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_user_name(self, first_name):
        self.set(PracticeFormLocators.first_name_field, first_name)

    def set_last_name(self, last_name):
        self.set(PracticeFormLocators.last_name_field, last_name)

    def set_email_name(self, email_name):
        self.set(PracticeFormLocators.email_name_field, email_name)

    def set_mobile_number(self, mobile_number):
        self.set(PracticeFormLocators.mobile_number_field, mobile_number)

    def click_date_of_birth(self):
        self.click(PracticeFormLocators.date_of_birth)

    def click_date_of_birth2(self):
        self.click(PracticeFormLocators.date_of_birth2)

    def click_submit_button(self):
        self.driver.execute_script("document.getElementById('submit').style.marginTop = '-600px';")
        self.click(PracticeFormLocators.submit_button)

    def fill_practice_form_information(self, first_name, last_name, email_name, mobile_number):
        self.set_user_name(first_name)
        self.set_last_name(last_name)
        self.set_email_name(email_name)
        self.set_mobile_number(mobile_number)
        self.click_date_of_birth()
        self.click_date_of_birth2()
        self.gender_select()
        self.hobbies_select()

    def form_is_displayed(self):
        return self.is_displayed(PracticeFormLocators.submitting_form)

    def gender_select(self):
        gender_field = self.find(*PracticeFormLocators.gender)
        self.driver.execute_script("arguments[0].checked = true;", gender_field)

    def hobbies_select(self):
        hobbies_field = self.find(*PracticeFormLocators.hobbies)
        self.driver.execute_script("arguments[0].checked = true;", hobbies_field)
