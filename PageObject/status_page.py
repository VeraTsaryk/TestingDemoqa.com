from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class StatusPage(BasePage):
    second_link_button = (By.CSS_SELECTOR,'#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > a:nth-child(14)')

    def __init__(self, driver):
        super().__init__(driver)

    def click_second_link_button(self):
        self.click(self.second_link_button)


