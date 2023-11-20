from PageObject.base_page import BasePage
from Locators.text_box_locators import TextBoxLocators


class TextBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def set_full_name(self, user_name):
        self.set(TextBoxLocators.full_name, user_name)

    def set_email_name(self, email_name):
        self.set(TextBoxLocators.email, email_name)

    def set_current_address(self, current_address_name):
        self.set(TextBoxLocators.current_address, current_address_name)

    def set_permanent_address(self, permanent_address_name):
        self.set(TextBoxLocators.permanent_address, permanent_address_name)

    def click_submit_button(self):
        self.click(TextBoxLocators.button_submit)

    @property
    def get_text_out_put_name(self):
        return self.get_text(TextBoxLocators.outputName)

    @property
    def get_text_out_put_email(self):
        return self.get_text(TextBoxLocators.outputEmail)

    @property
    def get_text_out_put_current_address(self):
        return self.get_text(TextBoxLocators.outputCurrentAddress)

    @property
    def get_text_out_put_permanent_address(self):
        return self.get_text(TextBoxLocators.outputPermanentAddress)
