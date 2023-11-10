from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class DialogsPage(BasePage):
    small_model = (By.ID, 'showSmallModal')
    large_model = (By.ID, 'showLargeModal')
    modal_title = (By.CLASS_NAME, 'modal-title')

    def __init__(self, driver):
        super().__init__(driver)

    def click_small_model(self):
        self.click(self.small_model)

    def open_page(self, url):
        return self.driver.get(url)


    def click_large_model(self):
        self.click(self.large_model)

    @property
    def get_text_modal_title(self):
        return self.get_text(self.modal_title)

