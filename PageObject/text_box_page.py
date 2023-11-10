from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    full_name = (By.ID, 'userName')
    email = (By.ID, 'userEmail')
    current_address = (By.ID, 'currentAddress')
    permanent_address = (By.ID, 'permanentAddress')
    button_submit = (By.ID, 'submit')
    outputName = (By.CSS_SELECTOR, '#output #name')
    outputEmail = (By.CSS_SELECTOR, '#output #email')
    outputCurrentAddress = (By.CSS_SELECTOR, '#output #currentAddress')
    outputPermanentAddress = (By.CSS_SELECTOR, '#output #permanentAddress')

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        return self.driver.get(url)

    def set_full_name(self, user_name):
        self.set(self.full_name, user_name)

    def set_email_name(self, email_name):
        self.set(self.email, email_name)

    def set_current_address(self, current_address_name):
        self.set(self.current_address, current_address_name)

    def set_permanent_address(self, permanent_address_name):
        self.set(self.permanent_address, permanent_address_name)

    def click_submit_button(self):
        self.click(self.button_submit)

    @property
    def get_text_out_put_name(self):
        return self.get_text(self.outputName)

    @property
    def get_text_out_put_email(self):
        return self.get_text(self.outputEmail)

    @property
    def get_text_out_put_current_address(self):
        return self.get_text(self.outputCurrentAddress)

    @property
    def get_text_out_put_permanent_address(self):
        return self.get_text(self.outputPermanentAddress)
