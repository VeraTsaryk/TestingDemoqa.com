from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage


class LoginPage(BasePage):
    email_address_field = (By.ID, "userName")
    password_field = (By.ID, "password")
    login_button = (By.ID, 'login')
    warning_message = (By.CLASS_NAME, 'mb-1')
    log_out_button = (By.CSS_SELECTOR, 'div[class = "text-right col-md-5 col-sm-12"] #submit')
    login_name = (By.ID, 'userName-value')
    user_form = (By.CSS_SELECTOR, '#userForm > div:nth-child(1)')
    actual_name = (By.ID, 'userName-value')

    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(self.email_address_field, email_address)
        # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    # return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        return self.get_text(self.warning_message)

    def open_page(self, url):
        return self.driver.get(url)

    def click_login_out_button(self):
        self.click(self.log_out_button)

    def profile_name(self):
        return self.find(self.login_name)

    def actual_form(self):
        return self.find(self.user_form)

    def find_actual_name(self):
        return self.find(self.actual_name)

    @property
    def get_text_actual_name(self):
        return self.get_text(self.actual_name)
