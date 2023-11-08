from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage


class BookPage(BasePage, LoginPage):
    book = (By.ID, 'see-book-Git Pocket Guide')
    add_to_collection_button = (By.CSS_SELECTOR, 'div[class = "text-right fullButton"] #addNewRecordButton')
    user_profile = (By.CSS_SELECTOR, '.accordion :nth-child(6) > div > ul> li:nth-child(3)')
    login_form = (By.ID, 'login')

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        return self.driver.get(url)

    def click_book(self):
        self.click(self.book)

    def click_add_to_collection_button(self):
        self.click(self.add_to_collection_button)

    def click_login_form(self):
        self.click(self.login_form)



