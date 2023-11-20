from PageObject.base_page import BasePage
from Locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(LoginLocators.email_address_field, email_address)
        # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set(LoginLocators.password_field, password)

    def click_login_button(self):
        self.click(LoginLocators.login_button)

    # return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        return self.get_text(LoginLocators.warning_message)

    def click_login_out_button(self):
        self.click(LoginLocators.log_out_button)

    def profile_name(self):
        return self.find(LoginLocators.login_name)

    def actual_form(self):
        return self.find(LoginLocators.user_form)

    def find_actual_name(self):
        return self.find(LoginLocators.actual_name)

    @property
    def get_text_actual_name(self):
        return self.get_text(LoginLocators.actual_name)

    def actual_name_is_displayed(self):
        return self.is_displayed(LoginLocators.actual_name)

    def user_form_is_displayed(self):
        return self.is_displayed(LoginLocators.user_form)
