from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from PageObject.login_page import LoginPage


class BookPage(LoginPage):
    book = (By.ID, 'see-book-Git Pocket Guide')
    add_to_collection_button = (By.CSS_SELECTOR, 'div[class = "text-right fullButton"] #addNewRecordButton')
    user_profile = (By.CSS_SELECTOR, '.accordion :nth-child(6) > div > ul> li:nth-child(3)')
    login_form = (By.ID, 'login')
    search_field = (By.ID, 'searchBox')
    login_button_in_profile = (By.CSS_SELECTOR, '#notLoggin-label > a:nth-child(1)')
    button_go_to_store = (By.ID, 'gotoStore')
    delete_button = (By.ID, 'delete-record-undefined')
    small_modal = (By.ID, 'closeSmallModal-ok')

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

    def click_user_profile(self):
        user_profile_field = self.find(self.user_profile)
        self.driver.execute_script("arguments[0].scrollIntoView()", user_profile_field)
        self.click(self.user_profile)

    def set_search_field(self,book_name):
        self.set(self.search_field, book_name)

    def click_login_button_in_profile(self):
        self.click(self.login_button_in_profile)

    def click_button_go_to_store(self):
        self.click(self.button_go_to_store)

    def click_delete_button(self):
        self.click(self.delete_button)

    def click_close_small_model(self):
        self.click(self.small_modal)