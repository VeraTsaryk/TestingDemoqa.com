from PageObject.base_page import BasePage
from Locators.age_locators import AgeLocators


class AgePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_rename_button(self):
        self.click(AgeLocators.rename_button)

    def set_age_field(self, age):
        self.set(AgeLocators.field_age, age)

    def click_submit_button(self):
        self.click(AgeLocators.submit_button)

    @property
    def get_text_field_age(self):
        return self.get_text(AgeLocators.edit_field_age)
