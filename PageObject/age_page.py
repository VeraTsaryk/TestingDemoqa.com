from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class AgePage(BasePage):
    edit_field_age = (By.CSS_SELECTOR, '.rt-tbody > div:nth-child(1) .rt-td:nth-child(3)')
    rename_button = (By.ID, 'edit-record-1')
    field_age = (By.ID, 'age')
    submit_button = (By.ID, 'submit')
    edit_field_age = (By.CSS_SELECTOR, '.rt-tbody > div:nth-child(1) .rt-td:nth-child(3)')

    def __init__(self, driver):
        super().__init__(driver)

    def click_rename_button(self):
        self.click(self.rename_button)

    def set_age_field(self, age):
        self.set(self.field_age, age)

    def click_submit_button(self):
        self.click(self.submit_button)

    def open_page(self, url):
        return self.driver.get(url)

    @property
    def get_text_field_age(self):
        return self.get_text(self.edit_field_age)
